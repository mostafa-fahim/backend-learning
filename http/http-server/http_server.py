from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):
    def send_text(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message)

    def do_GET(self):
        if self.path == "/":
            self.send_text(200, b"Home Page")

        elif self.path == "/users":
            self.send_text(200, b"Users Page")

        else:
            self.send_text(404, b"Page Not Found")


server = HTTPServer(("localhost", 8000), MyHandler)

print("My server is running on http://localhost:8000")

server.serve_forever()