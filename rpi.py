# this is the file you need to add the rpi code in
import requests

def get_product_by_rfid(rfid):
    url = f"http://localhost:8000/products/{rfid}"
    response = requests.request("GET", url)
    print(response.json())

# add the code to get the rfid tag from the rpi here and then call the get_product_by_rfid function and pass the rfid tag as the argument.