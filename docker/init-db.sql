-- Database initialization script for KNI Webapp
-- This runs when PostgreSQL container starts for the first time

-- Create additional databases if needed
-- (Main database is created by POSTGRES_DB environment variable)

-- Create extensions that might be needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For full-text search
CREATE EXTENSION IF NOT EXISTS "unaccent"; -- For accent-insensitive search

-- Set timezone
SET timezone = 'Europe/Copenhagen';

-- Log successful initialization
DO $$
BEGIN
    RAISE NOTICE 'KNI Webapp database initialized successfully';
END $$;