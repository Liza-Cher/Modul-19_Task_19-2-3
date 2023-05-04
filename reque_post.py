import requests
BASE_URL = "https://petstore.swagger.io/v2"
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