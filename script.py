import requests
import json

# this is the list of all products, you can add more products to this list
products ={

    1: {
    "product_name": "test",
    "price": "test",
    "rfid_tag": "test"
    },

    2: {
    "product_name": "test2",
    "price": "test2",
    "rfid_tag": "test2",
    }

}

def create_products(product):
    url = "http://localhost:8000/products"
    payload = product
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(response.json())

def get_all_products():
    url = "http://localhost:8000/products"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())


if __name__ == "__main__":

# if you want to create products uncomment the following lines
    # for product in products.values():
    #     create_products(product)

# if you want to get all products uncomment the following line
    # get_all_products()
