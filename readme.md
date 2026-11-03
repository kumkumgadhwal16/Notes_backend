Notes App API

A REST API backend for a Notes application built with FastAPI,
PostgreSQL, SQLAlchemy, and JWT authentication. The API can
be tested using the automatically generated Swagger UI and can later be
connected to an Android/Flutter frontend.

Features
- User registration with first name, last name, email, and password
- Password hashing before storing user credentials
- Login that returns a JWT access token
- JWT-protected Notes endpoints
- Create notes with a title or without a title
- List the logged-in user's notes
- Retrieve one note by ID
- Update a note using PATCH
- Delete a note
- User ownership checks so users can only access their own notes
- Interactive API documentation with Swagger UI

Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- PyJWT
- pwdlib / Argon2 password hashing
- Uvicorn

Project Structure
notes_fastapi/
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── notes.py
│   ├── __init__.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

Do not upload your actual .env file, virtual environment (venv/),
database passwords, or JWT secrets to GitHub.

Prerequisites

Install the following before running the project:
- Python
- PostgreSQL
- Git (optional, for version control)

Setup on Windows

1. Open the project folder
Open PowerShell or the VS Code terminal in the notes_fastapi
folder---the folder containing requirements.txt and the app
directory.
2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1
If PowerShell blocks activation, you can run the activation command in
Command Prompt instead:
venv\Scripts\activate.bat
3. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
4. Create the PostgreSQL database
Create a database named notes_db using pgAdmin or the PostgreSQL
command line. If you choose a different database name, use that name in
DATABASE_URL below.
5. Configure environment variables
Create a file named .env in the project root (next to
requirements.txt). Add your own local database credentials and a
strong, private JWT secret:
DATABASE_URL=postgresql+psycopg://YOUR_DB_USER:YOUR_DB_PASSWORD@localhost:5432/notes_db
JWT_SECRET_KEY=REPLACE_WITH_A_LONG_RANDOM_SECRET
Replace YOUR_DB_USER, YOUR_DB_PASSWORD, and the JWT secret with your
own values. Do not use the example values as real credentials. Keep
.env private and never commit it to GitHub.
6. Start the development server
Run this command from the project root:
uvicorn app.main:app --reload

The server should be available at:
- API health check: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json
The current development setup creates tables through SQLAlchemy at
application startup. For production, configure and use database
migrations (for example, Alembic) rather than relying on create_all().
API Endpoints
All Notes endpoints require a valid JWT access token.

  Method     Endpoint             Purpose
  GET      /                  Health check
  POST     /auth/register     Register a user
  POST     /auth/login        Log in and receive a JWT token
  POST     /notes             Create a note
  GET      /notes             List the logged-in user's notes
  GET      /notes/{note_id}   Retrieve one of the user's notes
  PATCH    /notes/{note_id}   Update a note
  DELETE   /notes/{note_id}   Delete a note
How to Test with Swagger UI
1. Start the server and open http://127.0.0.1:8000/docs.
2. Open POST /auth/register and register a test user.
3. Open POST /auth/login and log in with that user's email and
   password.
4. Copy the access_token from the login response.
5. Click Authorize and enter the token as required by the displayed
   authentication scheme. If the dialog asks for a bearer token, enter
   the token; if it explicitly asks for the full value, enter
   Bearer YOUR_TOKEN.
6. Test the Notes endpoints.
Example: Create a note
Send a request to POST /notes with a JSON body such as:
{
  "title": "FastAPI Practice",
  "content": "My first note from Swagger UI."
}
A note without a title can be created by sending:
{
  "title": null,
  "content": "A note without a title."
}
Example: Update a note
Send a request to PATCH /notes/{note_id}. For example, to update only
the title:
{
  "title": "Updated note title"
}
Common response codes
- 200 OK: request succeeded.
- 201 Created: a user or note was created.
- 204 No Content: note was deleted successfully; the response body
  is empty.
- 401 Unauthorized: authentication is missing or invalid.
- 404 Not Found: the note does not exist or does not belong to the
  logged-in user.
- 409 Conflict: the email is already registered.
- 422 Unprocessable Entity: request data failed validation.
Security Notes
- Passwords should never be stored as plain text.
- Keep .env and all secrets out of source control.
- Use a strong, unique JWT secret in every environment. If a secret or
  token has been exposed, rotate the secret and issue new tokens.
- The access token currently expires after 30 minutes.
- Use HTTPS and secure deployment settings outside local development.
- Review rate limiting, logging, database migrations, backups, and
  automated tests before production use.
Current Limitations / Future Improvements
Before treating this as production-ready, consider adding:
- Automated API tests with pytest and FastAPI's TestClient
- Alembic database migrations
- A sanitized .env.example file
- Improved production logging and consistent error handling
- Rate limiting and deployment configuration
- CI checks and a documented deployment process
- Integration testing with the actual Android/Flutter client
License
No license has been specified yet. Add a license file if you intend to
publish or distribute this project.