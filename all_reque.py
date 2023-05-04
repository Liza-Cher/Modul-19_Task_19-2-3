import requests
BASE_URL = "https://petstore.swagger.io/v2"
res = requests.get(f"{BASE_URL}/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

print("Статус ответа:", res.status_code)

if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

new_user = {
        # "id": 0,
        "username": "Liza_Pet",
        "firstName": "Liza",
        "lastName": "Petrova",
        "email": "Liza@gmail.com",
        "password": "Poiuyt321",
        "phone": "916-355-55-33",
        "userStatus": 0
}
res = requests.post(f"{BASE_URL}/user", headers={'accept': 'application/json'}, json=new_user)
print("Статус ответа:", res.status_code)
print(res.json())

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

res = requests.delete(f"{BASE_URL}/user/LenNon", headers={'accept': 'application/json'})
print("Статус ответа:", res.status_code)
print(res.json())