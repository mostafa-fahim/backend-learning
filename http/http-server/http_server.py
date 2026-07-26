# from http.server import HTTPServer, BaseHTTPRequestHandler

# class MyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-Type", "text/plain")
#         self.end_headers()
#         self.wfile.write(b"Hello from my server")


# server = HTTPServer(("localhost", 8000), MyHandler)

# print("Hello from my server")

# server.serve_forever()