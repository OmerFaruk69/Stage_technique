
import http.server
import socketserver

port = 82
#On met en paramettre l'host et le port
address = ("",port)
#Un simple gestionnaire
handler = http.server.SimpleHTTPRequestHandler
# On prépare notre serveur avec un protocol TCP 
https = socketserver.TCPServer(address,handler)
print(f"Server is running in the port {port}")
https.serve_forever()

