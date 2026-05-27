-- ========================================
-- SECRET SANTA DATABASE SETUP
-- ========================================
-- This file contains SQL queries to create the database and tables
-- for the Secret Santa application

-- ========================================
-- 1. CREATE DATABASE
-- ========================================
CREATE DATABASE IF NOT EXISTS secret_santa_db;

-- Switch to the database
USE secret_santa_db;

-- ========================================
-- 2. CREATE TABLES
-- ========================================

-- Table: secret_santa
-- Purpose: Store Secret Santa assignments
-- Columns:
--   - id: Unique identifier (Primary Key)
--   - participant_name: Name of the person participating
--   - assigned_to: Name of the person this participant is assigned to gift
--   - created_date: Date when the assignment was created
--   - created_time: Time when the assignment was created

CREATE TABLE IF NOT EXISTS secret_santa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    participant_name VARCHAR(100) NOT NULL,
    assigned_to VARCHAR(100) NOT NULL,
    created_date DATE NOT NULL,
    created_time TIME NOT NULL,
    INDEX idx_created_date (created_date),
    INDEX idx_participant_name (participant_name)
);

-- Table: wishlist
-- Purpose: Store user wishlists
-- Columns:
--   - id: Unique identifier (Primary Key)
--   - name: Name of the person who created the wishlist
--   - wishlist: The wishlist content (text with items and preferences)
--   - created_date: Date when the wishlist was created
--   - created_time: Time when the wishlist was created

CREATE TABLE IF NOT EXISTS wishlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    wishlist TEXT NOT NULL,
    created_date DATE NOT NULL,
    created_time TIME NOT NULL,
    INDEX idx_name (name),
    INDEX idx_created_date (created_date)
);

-- ========================================
-- 3. SAMPLE DATA (OPTIONAL)
-- ========================================
-- Uncomment below to add sample data for testing

-- INSERT INTO secret_santa (participant_name, assigned_to, created_date, created_time)
-- VALUES 
--   ('Alice', 'Charlie', CURDATE(), CURTIME()),
--   ('Bob', 'Alice', CURDATE(), CURTIME()),
--   ('Charlie', 'Bob', CURDATE(), CURTIME());

-- INSERT INTO wishlist (name, wishlist, created_date, created_time)
-- VALUES 
--   ('Alice', '- Wireless Headphones\n- Coffee Maker\n- Book: The Midnight Library', CURDATE(), CURTIME()),
--   ('Bob', '- Winter Jacket (Size M)\n- Running Shoes\n- Gaming Mouse', CURDATE(), CURTIME()),
--   ('Charlie', '- Scented Candles\n- Plant (Indoor)\n- Desk Lamp', CURDATE(), CURTIME());

-- ========================================
-- 4. VERIFICATION QUERIES
-- ========================================
-- Run these to verify the tables were created correctly

-- SELECT 'Tables created successfully!' AS status;
-- SHOW TABLES;
-- DESCRIBE secret_santa;
-- DESCRIBE wishlist;

-- ========================================
-- END OF SETUP
-- ========================================