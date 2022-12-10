# ESP8266-gestion-wifi
ESP8266 gestion du réseau wifi

#Access point

le fichier boot.py permet de définir la carte D1 mini en mode access point(hotspot). Le nom du SSID et la clé de sécurité sont définis

sources documentaires pour plus de paramètres:
https://docs.micropython.org/en/v1.19/library/network.WLAN.html

le fichier main.py permet de créer un serveur web par l'intermédiaire d'un socket.
la boucle écoute et répond aux requêtes http. la page html est définie dans la fonction web_page
