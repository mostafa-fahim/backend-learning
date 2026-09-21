                                    # HTTP API Server
I built an HTTP API server using Pyhton's http.server module for managing users.
I built this server to practice building HTTP API for managing the users using GET, POST, PUT, PATCH AND DELETE methods.

To run this server command python http_server.py on the terminal and then the server will run and keep listening to localhost:8000.

The endpoits you can use are:
Get / :for getting the homepage, server will return "Home Page" for it.

GET /users :for getting the users from users collection. The server will return 2 users containing on one page.
GET /users?page=2 :for getting the users from a specific page. You can add the page you want and then request. If that page exist, the server will return users of that page or else it's will return "Page Not Found.

GET /users/:id :for getting one specific user from the users collection. The server will return that specific user in JSON body.

POST /users :for creating a new user in the user collections. You have to send a valid JSON for that with valid "name" and "age" fields. Server will return the created user with an ID.
Example:
POST /users

Request:
{"name": "Fahim", "age": 25}

Response:
{"name": "Fahim", "age": 25, "id": 5}

Status Code:
201 Created

PUT /users/:id :for updating/replacing a specific user from the user collections. You have to send a valid JSON reqeust with both valid "name" and "age" fields. Then the server will return the replaced/updated user with an ID.

PATCH /users/:id :for updating/modifying an user from the user colletion. You have to send a valid JSON that contains valid "name" and "age" fields or any of them. The server will return the updated/modified user with an ID.

DELETE /users/:id :for deleting a specific user. Once you do that the server will return a seccess response saying "User Deleted".

The server returns status codes for each request:
200 for successfully processed requests
201 once you are successfully done creating an user
400 for a bad request/missing data
404 for request that is for resources that doesn't exist in the server