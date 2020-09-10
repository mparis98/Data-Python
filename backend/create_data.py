import requests, json, urllib

url = "https://opendata.datainfogreffe.fr/api/records/1.0/search/?dataset=societes-immatriculees-2020&q=&rows=10000&sort=date_immatriculation&facet=siren&facet=forme_juridique&facet=code_ape&facet=ville&facet=region&facet=greffe&facet=date_immatriculation&facet=statut&refine.date_immatriculation=2020-06"
urlCodeApe = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=nomenclature-dactivites-francaise-naf-rev-2&rows=1707&q=&facet=intitule_naf&facet=intitule_naf_65&facet=intitule_naf_40"

r = requests.get(url)
datas = r.json()
mylist = []
for data in datas['records']:
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
    if 'code_ape' in data['fields'].keys() and 'siren' in data['fields'].keys() and 'region' in data['fields'].keys():
        code_ape = data['fields']['code_ape']
        mylist.append({
            'siren':data['fields']['siren'],
            'denomination':data['fields']['denomination'],
            'region':data['fields']['region'],
            'ville':ville,
            'code_postal':code_postal,
            'num_dept':num_dept,
            'date_immatriculation':data['fields']['date_immatriculation'],
            'code_ape':code_ape,
            'fiche_identite':'https://www.infogreffe.fr/infogreffe/ficheIdentite.do?siren='+data['fields']['siren']
        })


rCodeApe = requests.get(urlCodeApe)
datasCodeApes = rCodeApe.json()
mylistCodeApe = []
for datasCodeApe in datasCodeApes['records']:
    if 'code_naf' in datasCodeApe['fields'].keys():
        code_ape = datasCodeApe['fields']['code_naf']
    else:
        code_ape = None
    if 'intitule_naf' in datasCodeApe['fields'].keys():
        intitule_naf = datasCodeApe['fields']['intitule_naf']
    else:
        intitule_naf = None
    if 'code_naf' in datasCodeApe['fields'].keys():
        code_ape = datasCodeApe['fields']['code_naf']
        mylistCodeApe.append({
            'code_ape':datasCodeApe['fields']['code_naf'],
            'intitule_naf':datasCodeApe['fields']['intitule_naf']
        })

for row in mylist:
    requests.post('http://localhost:5000/company/', json=row)

for row in mylistCodeApe:
    requests.post('http://localhost:5000/codeape/', json=row)
