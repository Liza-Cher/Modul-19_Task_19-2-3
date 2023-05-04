import requests
BASE_URL = "https://petstore.swagger.io/v2"
data = {
        "id": 0,
        "username": "LenNon",
        "firstName": "Lena",
        "lastName": "NotaName",
        "email": "Lena@gmail.com",
        "password": "Qwert1234",
        "phone": "917-777-77-77",
        "userStatus": 0
}
res = requests.put(f"{BASE_URL}/user/Liza_Pet", headers={'accept': 'application/json'}, json=data)
print("Статус ответа:", res.status_code)
print(res.json())
