-- Create table to store user info
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    place TEXT NOT NULL,
    password TEXT NOT NULL  -- 📝 TODO: Rename this to password_hash
);

-- 📝 TODO: For existing DBs, run this once manually and then comment it
-- ALTER TABLE users RENAME COLUMN password TO password_hash;
