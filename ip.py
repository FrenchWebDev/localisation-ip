import socket 
import requests
from gmplot import gmplot
import json

ip_address = "109.212.44.233"
try:
   socket.inet_aton(ip_address)
   print("Valid IP address")

   request_url = 'https://geolocation-db.com/jsonp/' + ip_address
   response = requests.get(request_url)
   result = response.content.decode()
   result = result.split("(")[1].strip(")")
   result  = json.loads(result)
   city = result['country_name']
   print(city)
   
except socket.error:
   print("Invalid IP")