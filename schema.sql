-- Create table to store user info
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    -- 📝 TODO: Add column for role
    -- 📝 TODO: Add column for place
    password TEXT NOT NULL
);
