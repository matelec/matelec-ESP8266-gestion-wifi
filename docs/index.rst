ACCESS POINT
=======================

**sources documentaires pour plus de paramètres:**
https://docs.micropython.org/en/v1.19/library/network.WLAN.html

La création d'un point d'accès s'effectue à l'aide de 4 lignes de code. Elles sont à placer dans le script boot.py de la carte D1 mini 

importer la librairie network
::
        import network
définir l’interface ap en mode AP
::
        ap = network.WLAN(network.AP_IF)
activé l’interface ap:
::
        ap.active(True)
définir les paramètres de l’interface ap
::
        ap.config(essid=‘xxxxx’, password=‘xxxxxx’)









sources documentaires pour plus de paramètres:
https://docs.micropython.org/en/v1.19/library/network.WLAN.html

le fichier main.py permet de créer un serveur web par l'intermédiaire d'un socket.
la boucle écoute et répond aux requêtes http. la page html est définie dans la fonction web_page
