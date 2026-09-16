from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

users = []


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
                number = int(page[0])

            if number == 1:
                self.send_text(200, "application/json", b'[{"name": "Karim", "age": 21}, {"name": "Ahmed", "age": 22}]')
            elif number == 2:
                self.send_text(200, "application/json", b'[{"name": "Rahim", "age": 26}, {"name": "Sakib", "age": 29}]')
            else:
                self.send_text(404, "text/plain", b"Page Not Found")

        elif path.startswith("/users/"):
            parts = path.split("/")
            user_id = parts[2]

            if user_id == "1":
                self.send_text(200, "application/json", b'{"name": "Karim", "age": 21}')
            elif user_id == "2":
                self.send_text(200, "application/json", b'{"name": "Ahmed", "age": 22}')
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

        users.append(data)

        print(users)

        self.send_text(201, "text/plain", b"POST received")


server = HTTPServer(("localhost", 8000), MyHandler)

print("My server is running on http://localhost:8000")

server.serve_forever()