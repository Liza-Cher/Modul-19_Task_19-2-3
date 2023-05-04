# import requests
# status='available'
# res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
# print(res.status_code)
# print(res.text)
# print(res.json())
#####################################
import requests
BASE_URL = "https://petstore.swagger.io/v2"
res = requests.get(f"{BASE_URL}/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

print("Статус ответа:", res.status_code)

if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)






