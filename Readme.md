# Intro
- Git: A version control tool that helps track code changes and collaborate with others.
- Branch: A separate workspace in Git where you can make changes without affecting the main code.
- Git add, commit: Save changes in git `git add .; git commit -m "add solution"`
- Git Checkout: Move to a different branch. `git checkout 02-hello-api-time`
- Website: A collection of web pages accessible through a browser, typically hosted on a server.
- Static Site: A website with fixed content that doesn’t change unless manually updated (like our index.html).
- HTML (HyperText Markup Language): The structure of a webpage—defines elements like headings, paragraphs, and links.
- Browser: The software (Chrome, Firefox, Edge) that loads and displays websites.

# 02-hello-api-time
- Server: A computer that hosts websites and serves them to users over the internet.
- Port: A numbered communication endpoint on a server (e.g., :80 for websites, :443 for HTTPS).
- pip: Python's package installer. Used to install libraries like FastAPI.
- venv: Virtual environment to isolate dependencies per project.
- requirements.txt: Lists Python dependencies for others (or yourself) to install easily.
- FastAPI: A Python framework to build APIs quickly and clearly.
- uvicorn: ASGI server that runs FastAPI apps. Like a lightweight web server. (FastAPI ↔ uvicorn ↔ Browser)
- ASGI (Asynchronous Server Gateway Interface): a standard that defines how python webapps(like FastAPI apps) talk to web servers(like uvicorn). Better suited for async, SSE, websockets than (traditional) WSGI.
- uvicorn main:app means: use "uvicorn" webserver to run the FastAPI "app" defined in "main.py"
- uvicorn main:app --reload: reload server on file changes
- @app.get(...)	Tells FastAPI to handle GET requests at the given path
- datetime.now(): Gets current time.

# 03-query-param-greet
- Query Param: Part of URL that sends optional data to server. Comes after ? in URL.
- Swagger UI:	Auto-generated interactive docs for your API at /docs. Comes built-in with FastAPI.
- OpenAPI:	Industry standard spec for describing REST APIs. FastAPI uses this under the hood.
- POST: HTTP method used to send data to the server — typically with a body (JSON, form, etc.)

# 04-post-store-user
- @app.post(): Declares a POST endpoint in FastAPI
- Path Parameter: Declared like /api/users/{id}. Usually used to fetch/update/delete specific resources
- Type Annotations in Python: Type annotations let you specify variable/function types (like str, int, dict). Optional. 
- Type Annotations in FastAPI: FastAPI relies on them to determine how to parse input, so not optional in FastAPI context.
- FastAPI - Query param vs Body param vs Path param: FastAPI uses type annotations to automatically determine where to extract each parameter from.
	- Simple types (str, int) → query/path param (based on route)
	- Complex types (dict, Pydantic model) → body param (for POST, PUT, etc.)
- REST (Representational State Transfer): A set of conventions for designing clean and predictable APIs around resources.
- Resources & URLs: Each type of object (like users) is treated as a resource.
    - /api/users → collection (many users)
    - /api/users/1 → specific user with ID 1

# 05-put-delete-user
- PUT: HTTP method used to update a resource
- DELETE: HTTP method used to delete a resource
- CRUD: Stands for Create(POST), Read(GET), Update(PUT), Delete(DELETE) — the four fundamental operations of persistent storage.

# 06-validate-input
- HTTP Status Codes: 
	- 200: OK
	- 201: Created (used when new resource is saved)
	- 400: Bad Request (input error)
	- 404: Not Found
	- 500: Internal Server Error (your app crashed)
- JSONResponse: Used to send custom responses with status codes and structured JSON

# 07-validate-with-pydantic
- Pydantic: A data validation library used by FastAPI to define and validate request/response models using Python types. It's like a data gatekeeper - guarantees clean, typed data in and out.
- BaseModel: The base class in Pydantic from which all models should inherit.
- Field(...): Used to add validation rules (e.g., min/max length, default values) on model fields.
- Literal[...]: Used to restrict a field to specific allowed values. Great for enums like job roles.

# 08-setup-db-postgres
- Docker: A tool to run apps in lightweight containers that bundle code + dependencies. Great for consistent environments.
- Docker Compose: Lets you define and run multi-container setups (like app + db) using a simple docker-compose.yml.
- Postgres: A popular open-source SQL database used to store structured data like users, messages, etc.
- Environment Variables: Helps keep secrets/config out of the main file
- Volumes: Used to persist database data even if the container is stopped or deleted.
	- If you want to delete volume: docker compose down -v & start again docker compose up 
- Container Name: A label you give your container so it’s easier to refer to (e.g. interview-db).
- Port Mapping: "5433:5432" makes DB accessible on localhost:5433
- POSTGRES_DB / POSTGRES_USER / POSTGRES_PASSWORD: Special env vars used by the official Postgres Docker image. Must use these exact names.
- SELECT NOW(): Postgres command that returns current DB time.
- psycopg2: A Python library to interact with Postgres DB.
- os.getenv(...): Fetch values from environment variables — clean way to keep secrets/configs outside code.
- .env vs docker.env:
    • .env → used by FastAPI app
    • docker.env → used by Docker Compose
- Database Connection: A live link between your app and the database — like opening a door to enter the DB.
- Cursor: Once inside, the cursor lets you run SQL queries and fetch results. Think of it as your command line session inside the DB.
- cursor.close(): Tells Postgres you're done running queries. Frees up the server-side resources(process/thread, memory, locks, etc.) for that session.
- connection.close(): Properly ends the DB session and releases the connection slot. Avoids exhausting the DB's limited pool of concurrent connections.

# 09-connect-app-to-db
- CREATE TABLE: SQL command to define your table structure
- SERIAL: Auto-incrementing integer — useful for user id
- conn.commit(): Makes sure changes (like INSERT) are saved
- cur.fetchone(): Gets one row from SELECT result
- CREATE TABLE IF NOT EXISTS: Ensures table is created only if it doesn’t already exist
- @app.on_event("startup"): Used to run code that needs to run once when app starts
- INSERT INTO users (...) VALUES (...) RETURNING id: Saves user and gives back the new ID
- lifespan (FastAPI): Modern way to run setup/teardown logic (like DB init) during app startup/shutdown. Replaces deprecated @app.on_event("startup").
- asynccontextmanager: Lets you define async-compatible setup/teardown blocks using yield — used with lifespan to run startup logic once.

# 11-secure-password
- Schema Migration (manual): To change an existing table, use ALTER TABLE. E.g., ALTER TABLE users ADD COLUMN password_hash TEXT;
- Passlib: Library used for hashing passwords (to store it securely).
- Why response_model? - This forces a clean API contract and auto-docs it. (Eg: Returning raw DB data can leak sensitive fields.)

# 12-use-sqlalchemy
- SQLAlchemy ORM: Lets you define tables as Python classes, and rows as objects.
- Why ORM: Cleaner code, safer queries, reusable models, and fewer errors.
- Base.metadata.create_all(): Auto-creates all tables defined using the ORM.
- Session: SQLAlchemy’s interface to run queries, insert rows, commit, etc.

# 13-sqlalchemy-crud
- SessionLocal(): Creates a new SQLAlchemy session for talking to the DB
- query().filter().first(): Searches for matching user and returns first (or None)
- db.commit(): Saves changes to the DB. Can be used to batch multiple changes, rollback if required.
- db.refresh(obj): Reloads object from DB to get latest state after insert/update
- .all(): Fetches all matching records — returns list
- orm_mode = True: Tells Pydantic to convert SQLAlchemy models to response schemas
