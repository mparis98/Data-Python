import requests, json, urllib

url = "https://opendata.datainfogreffe.fr/api/records/1.0/search/?dataset=societes-immatriculees-2020&q=&rows=2500&sort=date_immatriculation&facet=siren&facet=forme_juridique&facet=code_ape&facet=ville&facet=region&facet=greffe&facet=date_immatriculation&facet=statut"

r = requests.get(url)
datas = r.json()
mylist = []
for data in datas['records']:
    if 'region' in data['fields'].keys():
        region = data['fields']['region']
    else:
        region = None
    if 'ville' in data['fields'].keys():
        ville = data['fields']['ville']
    else:
        ville = None
    if 'code_postal' in data['fields'].keys():
        code_postal = data['fields']['code_postal']
    else:
        code_postal = None
    if 'num_dept' in data['fields'].keys():
        num_dept = data['fields']['num_dept']
    else:
        num_dept = None
    if 'code_ape' in data['fields'].keys():
        code_ape = data['fields']['code_ape']
        mylist.append({
            'siren':data['fields']['siren'],
            'denomination':data['fields']['denomination'],
            'region':region,
            'ville':ville,
            'code_postal':code_postal,
            'num_dept':num_dept,
            'date_immatriculation':data['fields']['date_immatriculation'],
            'code_ape':code_ape,
            'fiche_identite':'https://www.infogreffe.fr/infogreffe/ficheIdentite.do?siren='+data['fields']['siren']
        })

for row in mylist:
    requests.post('http://localhost:5000/company/', json=row)
