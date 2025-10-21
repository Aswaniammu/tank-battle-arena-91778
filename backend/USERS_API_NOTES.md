# Users API Notes

Endpoints:
- GET `/users` — List users
- POST `/users` — Create a new user

Example:
- Create:
  curl -X POST http://localhost:3001/users -H "Content-Type: application/json" -d '{"username":"player1"}'
- List:
  curl http://localhost:3001/users
