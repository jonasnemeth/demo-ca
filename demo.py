import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer


class Demo(BaseHTTPRequestHandler):
    def do_GET(self):
        body = """<!doctype html><meta charset="utf-8">
        <title>CA-Demo</title>
        <h1>CA Funktioniert</h1>
        </body>""".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(("127.0.0.1", 8443), Demo)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("localhost.crt", "localhost.key")
server.socket = context.wrap_socket(server.socket, server_side=True)
print("https://localhost:8443")
server.serve_forever()
