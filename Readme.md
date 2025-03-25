💭 How to give coach some persistent memory?
Add a Postgres database using Docker Compose.

🎯 Problem  
Set up Postgres using Docker Compose.

⚙️ Your Task
- Create a `docker.env` file to set DB name, username and password (see sample.docker.env)
- Complete `docker-compose.yml` to spin up a Postgres DB

🧪 Test
- Run: `docker compose up`
- Connect to the DB:
  - `docker exec -it <container_name> psql -U <your_user> -d <your_db>`
  - Run a SQL command like: `SELECT NOW();`

Note: `docker compose down -v` if you want remove previously created volume. 
If you created the DB and decide to change the user name/password, you can run `down -v` first and then `up`.
