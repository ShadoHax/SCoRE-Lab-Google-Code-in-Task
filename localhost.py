import http.server
import socketserver
port = 8080
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), handler) as https:
    https.serve_forever()