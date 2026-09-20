import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

users = [
    {"id": 1, "name": "Karim", "age": 21},
    {"id": 2, "name": "Ahmed", "age": 22},
    {"id": 3, "name": "Rahim", "age": 26},
    {"id": 4, "name": "Sakib", "age": 29},
]


class MyHandler(BaseHTTPRequestHandler):
    def send_text(self, status_code, content_type, message):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(message)

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path == "/":
            self.send_text(200, "text/plain", b"Home Page")

        elif path == "/users":
            page = query_params.get("page")

            if page is None:
                number = 1
            else:
                try:
                    number = int(page[0])
                except ValueError:
                    self.send_text(400, "text/plain", b"Page must be an int")
                    return

            start = (number - 1) * 2
            end = start + 2
            page_users = users[start:end]

            if not page_users:
                self.send_text(404, "text/plain", b"Page Not Found")
                return
            
            response = json.dumps(page_users).encode()
            self.send_text(200, "application/json", response)

        elif path.startswith("/users/"):
            parts = path.split("/")

            try:
                user_id = int(parts[2])
            except ValueError:
                self.send_text(400, "text/plain", b"User ID must be an int")
                return

            for user in users:
                if user["id"] == user_id:
                    response = json.dumps(user).encode()
                    self.send_text(200, "application/json", response)
                    return
            else:
                self.send_text(404, "text/plain", b"User Not Found")

        else:
            self.send_text(404, "text/plain", b"Page Not Found")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self.send_text(400, "text/plain", b"Invalid JSON")
            return

        if "name" not in data or "age" not in data:
            self.send_text(400, "text/plain", b"Missing required fields")
            return

        if not isinstance(data["name"], str):
            self.send_text(400, "text/plain", b"Name must be a str")
            return
        
        if not isinstance(data["age"], int):
            self.send_text(400, "text/plain", b"Age must be an int")
            return

        data["id"] = len(users) + 1
        users.append(data)

        response = json.dumps(data).encode()
        self.send_text(201, "application/json", response)

    def do_PUT(self):
        path = self.path

        if path.startswith("/users/"):
            parts = path.split("/")

            try:
                user_id = int(parts[2])
            except ValueError:
                self.send_text(400, "text/plain", b"User ID must be an int")
                return
            
            for user in users:
                if user["id"] == user_id:
                    content_length = int(self.headers["Content-Length"])
                    body = self.rfile.read(content_length)

                    try:
                        data = json.loads(body)
                    except json.JSONDecodeError:
                        self.send_text(400, "text/plain", b"Invalid JSON")
                        return

                    if "name" not in data or "age" not in data:
                        self.send_text(400, "text/plain", b"Missing required fields")
                        return

                    if not isinstance(data["name"], str):
                        self.send_text(400, "text/plain", b"Name must be a str")
                        return

                    if not isinstance(data["age"], int):
                        self.send_text(400, "text/plain", b"Age must be an int")
                        return

                    user["name"] = data["name"]
                    user["age"] = data["age"]

                    response = json.dumps(user).encode()
                    self.send_text(200, "application/json", response)
                    return
            else:
                self.send_text(404, "text/plain", b"User Not Found")
        else:
            self.send_text(404, "text/plain", b"Page Not Found")     

    def do_PATCH(self):
        path = self.path

        if path.startswith("/users/"):
            parts = path.split("/")

            try:
                user_id = int(parts[2])
            except ValueError:
                self.send_text(400, "text/plain", b"User ID must be an int")
                return

            for user in users:
                if user["id"] == user_id:
                    content_length = int(self.headers["Content-Length"])
                    body = self.rfile.read(content_length)

                    try:
                        data = json.loads(body)
                    except json.JSONDecodeError:
                        self.send_text(400, "text/plain", b"Invalid JSON")
                        return

                    if not data:
                        self.send_text(400, "text/plain", b"No fields to update")
                        return

                    if "name" in data and not isinstance(data["name"], str):
                        self.send_text(400, "text/plain", b"Name must be a str")
                        return
                    
                    if "age" in data and not isinstance(data["age"], int):
                        self.send_text(400, "text/plain", b"Age must be an int")
                        return

                    if "name" in data:
                        user["name"] = data["name"]

                    if "age" in data:
                        user["age"] = data["age"]

                    response = json.dumps(user).encode()
                    self.send_text(200, "application/json", response)
                    return
            else:
                self.send_text(404, "text/plain", b"User Not Found")
        else:
            self.send_text(404, "text/plain", b"Page Not Found")
                
server = HTTPServer(("localhost", 8000), MyHandler)

print("My server is running on http://localhost:8000")

server.serve_forever()