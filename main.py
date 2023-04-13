import requests

r = requests.post("http://127.0.0.1:8000/en/checkout/create-checkout-session/")

print(r.text)
