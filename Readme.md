# 08-setup-db-postgres

## 🎯 Problem
Set up Postgres using Docker Compose.

## ⚙️ Your Task
- Create a `docker-compose.yml` to spin up a Postgres DB
- Create a `.env` file to store DB name, username and password (see sample.env)
- Run the container and test connectivity

## 🧪 Test
- Run: `docker compose up`
- Verify container is running: `docker ps`
- Connect to the DB:
  - `docker exec -it <container_name> psql -U <your_user> -d <your_db>`
  - Run a SQL command like: `SELECT NOW();`

## 📦 Starter Code
- `sample.env`
- `docker-compose.yml`