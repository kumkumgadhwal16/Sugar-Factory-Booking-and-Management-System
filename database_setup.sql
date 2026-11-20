-- ═══════════════════════════════════════════════════════════════
-- Sugar Factory Booking System — MySQL Database Setup
-- Run this BEFORE running Django migrations.
-- ═══════════════════════════════════════════════════════════════

-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS sfbs
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Step 2: Use it
USE sfbs;

-- Step 3: Create a dedicated MySQL user (recommended for production)
-- Change 'your_password' to a strong password.
-- Comment out if using root locally.
-- CREATE USER IF NOT EXISTS 'sfbs_user'@'localhost' IDENTIFIED BY 'your_password';
-- GRANT ALL PRIVILEGES ON sfbs.* TO 'sfbs_user'@'localhost';
-- FLUSH PRIVILEGES;

-- ─── NOTE ───────────────────────────────────────────────────────
-- All tables (user, user_info, booking, etc.) are created
-- automatically by Django's migration system:
--
--   python manage.py migrate
--
-- This file only creates the database itself.
-- ────────────────────────────────────────────────────────────────

-- Verify
SELECT 'Database sfbs is ready. Now run: python manage.py migrate' AS status;
