import time
from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse 
import json

import pandas as pd, numpy as np
import random,requests
from bs4 import BeautifulSoup
from faker import Faker

HOST_NAME = '127.0.0.1' # server locale che risponde sulla porta 9000
PORT_NUMBER = 9000 # numero porta


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        
        

        s.send_response(200)
        s.send_header('Content-type', 'application/json')
        s.end_headers()
        #s.wfile.write(bytes("<html><head><title>Title goes here.</title></head>","utf8"))
        #s.wfile.write(bytes("<body><p>This is a test.</p>","utf8"))
        # s.path contine il percorso: 127.0.0.1:9000 contiene /,
        # il percorso s.path contiene "/percorso/sotto", se 127.0.0.1:9000/percorso/sotto 
        #s.wfile.write(bytes("<p>You accessed path: %s</p>" % s.path,"utf8"))
        #s.wfile.write(bytes("</body></html>","utf8"))
        
        
        
        path = s.path
        results = 1
        if '?' and '=' in path:
            query = urlparse(s.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            
            if 'results' in query_components:
                results = query_components["results"]
                print ("Results impostato!")
            else:
                print ("parametro results *NON* impostato")
           
        else:
            print ("parametro results *NON* impostato")
        print (results)
        fake = Faker()
        persone = {"persone":[]}
        n_persone = int(results)
        for n in range(n_persone):
            persona={"nome":fake.first_name(),"cognome":fake.last_name()}
            persone["persone"].append(persona)
        y = json.dumps(persone)
        s.wfile.write(bytes(y,"utf8"))


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print (time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print (time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))