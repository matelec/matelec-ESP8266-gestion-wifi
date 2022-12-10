def web_page():
  html = """ <!DOCTYPE html>
    <html>
    <body style="background-color:powderblue;">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
      <body>
      <h1 style="color:blue;">Hello, World!</h1>
      <p style="font-family:courier;">Ceci est la page du serveur web ESPRATTE</p>
      </body>
    </html>"""
  return html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    print("Attente d'une connexion client")
    connexionClient, adresse = s.accept()
    connexionClient.settimeout(4.0)
    print("Connecté avec le client", adresse)

    print("Attente requete du client")
    requete = connexionClient.recv(1024)     #requête du client
    requete = str(requete)
    print("Requete du client = ", requete)
    connexionClient.settimeout(None)

    print("Envoi reponse du serveur : code HTML a afficher")
    connexionClient.send('HTTP/1.1 200 OK\n')
    connexionClient.send('Content-Type: text/html\n')
    connexionClient.send("Connection: close\n\n")
    reponse = web_page()
    connexionClient.sendall(reponse)
    connexionClient.close()
    print("Connexion avec le client fermee")
    
