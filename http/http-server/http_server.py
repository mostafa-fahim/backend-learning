from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):

    def send_text(self, status_code, content_type, message):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(message)

    def do_GET(self):
        if self.path == "/":
            self.send_text(200, "text/plain", b"Home Page")

        elif self.path == "/users":
            self.send_text(200, "application/json", b'[{"name": "Karim", "age": 22}, {"name": "Ahmed", "age": 21}]')

        else:
            self.send_text(404, "text/plain", b"Page Not Found")


server = HTTPServer(("localhost", 8000), MyHandler)

print("My server is running on http://localhost:8000")

server.serve_forever()