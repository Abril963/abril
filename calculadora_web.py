import http.server
import socketserver
from pathlib import Path

PORT = 8000
WEB_DIR = Path(__file__).with_name("web")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

if __name__ == "__main__":
    print(f"Iniciando servidor web en http://localhost:{PORT}/")
    print("En GitHub Codespaces, expón el puerto 8000 en la sección Ports.")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Servidor detenido.")
