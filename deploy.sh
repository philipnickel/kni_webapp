#!/bin/bash

# Deployment script for KNI Webapp on Ubuntu VPS
# Run this script on your VPS after cloning the repository

set -e

PROJECT_NAME="kni_webapp"
PROJECT_DIR="/var/www/$PROJECT_NAME"
VENV_DIR="$PROJECT_DIR/venv"
USER="www-data"

echo "🚀 Deploying KNI Webapp..."

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root (use sudo)"
   exit 1
fi

# Install system dependencies
echo "📦 Installing system dependencies..."
apt update
apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib nginx supervisor git

# Create project directory
echo "📁 Setting up project directory..."
mkdir -p $PROJECT_DIR
cd $PROJECT_DIR

# Clone or update repository (you'll need to adjust the git URL)
if [ ! -d ".git" ]; then
    echo "📥 Cloning repository..."
    git clone https://github.com/philipnickel/kni_webapp.git .
else
    echo "🔄 Updating repository..."
    git pull origin main
fi

# Create virtual environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# Install Python dependencies
echo "📚 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Set up PostgreSQL database
echo "🗄️ Setting up PostgreSQL database..."
sudo -u postgres psql << EOF
CREATE DATABASE $PROJECT_NAME;
CREATE USER kni_user WITH PASSWORD 'your_db_password_here';
GRANT ALL PRIVILEGES ON DATABASE $PROJECT_NAME TO kni_user;
ALTER USER kni_user CREATEDB;
\q
EOF

# Copy environment file (you'll need to edit this manually)
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.production .env
    echo "⚠️  IMPORTANT: Edit .env file with your actual values!"
fi

# Set permissions
echo "🔒 Setting up permissions..."
chown -R $USER:$USER $PROJECT_DIR
chmod -R 755 $PROJECT_DIR

# Run Django commands
echo "🗃️ Running Django setup..."
cd $PROJECT_DIR
source $VENV_DIR/bin/activate
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py seed_tenant johann --admin-user JCleemannByg --admin-password admin123 --admin-email johann@jcleemannbyg.dk || true
python manage.py ensure_tenant_site --schema=johann --hostname=jcleemannbyg.dk --port=80

echo "✅ Deployment complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your actual values"
echo "2. Configure nginx (nginx config will be created separately)"
echo "3. Set up systemd service"
echo "4. Configure your domain DNS"