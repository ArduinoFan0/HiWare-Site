import http.server
import socketserver
from threading import Thread

PORT = 8081

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
def serve_thread():
    print("serving at port", PORT)
    httpd.serve_forever()
serving_thread = Thread(target=serve_thread)
serving_thread.start()

while True:
    text = input("type 'q' to quit")
    if text == "q":
        httpd.shutdown()
        httpd.server_close()
        break