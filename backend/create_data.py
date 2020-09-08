import requests


datas = [
    {'name': 'Blackberry'},
    {'name': 'Bip'},
    {'name': 'Walkman'},
    {'name': 'Discman'},
]


for data in datas:
    requests.post('http://localhost:5000/company/add', data=data)
