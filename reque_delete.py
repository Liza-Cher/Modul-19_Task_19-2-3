import requests
BASE_URL = "https://petstore.swagger.io/v2"

res = requests.delete(f"{BASE_URL}/user/LenNon", headers={'accept': 'application/json'})
print("Статус ответа:", res.status_code)
print(res.json())
