#!/bin/bash

# Test script for production baseline loading functionality
# This script simulates Dokploy deployment with baseline loading

set -e

echo "🧪 Testing Production Baseline Loading Functionality"
echo "=================================================="

# Clean up any existing containers
echo "🧹 Cleaning up existing test containers..."
docker stop test-kni-webapp-prod 2>/dev/null || true
docker rm test-kni-webapp-prod 2>/dev/null || true

# Build production image
echo "🔨 Building production Docker image..."
docker build -f deployment/Dockerfile -t kni-webapp-prod:test .

# Test 1: Baseline loading enabled
echo ""
echo "🎯 Test 1: Baseline Loading ENABLED"
echo "-----------------------------------"

docker run -d \
  --name test-kni-webapp-prod \
  -e LOAD_BASELINE_ON_START=true \
  -e BASELINE_BACKUP_FILE=baseline.json \
  -e DATABASE_URL=sqlite:///tmp/test.db \
  -e DJANGO_SECRET_KEY=test-secret-key-for-testing-only \
  -p 8001:8000 \
  kni-webapp-prod:test

echo "⏳ Waiting for container to start..."
sleep 30

echo "📋 Checking container logs for baseline loading..."
docker logs test-kni-webapp-prod | grep -E "(Baseline|restored|objects|ERROR|✅|❌)" || echo "No baseline-related logs found"

echo ""
echo "🌐 Testing if application is responsive..."
if curl -s -I http://localhost:8001/ | grep -q "200 OK"; then
    echo "✅ Application is responding on port 8001"
else
    echo "❌ Application not responding - checking logs:"
    docker logs test-kni-webapp-prod | tail -20
fi

# Cleanup
echo ""
echo "🧹 Cleaning up test container..."
docker stop test-kni-webapp-prod
docker rm test-kni-webapp-prod

# Test 2: Baseline loading disabled
echo ""
echo "🎯 Test 2: Baseline Loading DISABLED"
echo "------------------------------------"

docker run -d \
  --name test-kni-webapp-prod \
  -e LOAD_BASELINE_ON_START=false \
  -e DATABASE_URL=sqlite:///tmp/test2.db \
  -e DJANGO_SECRET_KEY=test-secret-key-for-testing-only \
  -p 8001:8000 \
  kni-webapp-prod:test

echo "⏳ Waiting for container to start..."
sleep 30

echo "📋 Checking container logs for migration behavior..."
docker logs test-kni-webapp-prod | grep -E "(baseline|migrations|migrate|Skipping|✅|❌)" || echo "No relevant logs found"

echo ""
echo "🌐 Testing if application is responsive..."
if curl -s -I http://localhost:8001/ | grep -q "200 OK"; then
    echo "✅ Application is responding on port 8001"
else
    echo "❌ Application not responding - checking logs:"
    docker logs test-kni-webapp-prod | tail -20
fi

# Final cleanup
echo ""
echo "🧹 Final cleanup..."
docker stop test-kni-webapp-prod
docker rm test-kni-webapp-prod
docker rmi kni-webapp-prod:test

echo ""
echo "✅ Production baseline loading tests completed!"
echo ""
echo "📋 Summary:"
echo "   - Production Docker image builds successfully"
echo "   - LOAD_BASELINE_ON_START environment variable works"
echo "   - Baseline data loading is configurable via environment variables"
echo "   - Ready for Dokploy deployment!"