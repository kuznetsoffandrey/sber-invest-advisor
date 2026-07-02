import http.server
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

print(f"Serving on port {PORT}")
http.server.HTTPServer(("", PORT), Handler).serve_forever()
