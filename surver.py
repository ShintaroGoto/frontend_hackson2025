from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # すべてのリクエストに対してファイル配信 or HTML配信
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("index.html", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
        else:
            # BGMファイルやfaviconなどはそのまま配信
            super().do_GET()
        

server_address = ("", 8080)
httpd = HTTPServer(server_address, MyHandler)
print("http://localhost:8080/ にアクセスしてください。")
httpd.serve_forever()
