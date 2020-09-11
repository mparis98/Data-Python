# Project flask end VueJS

Flask api Rest and VueJS.

## Initialize BDD

### Automatic (creat also creat database with value)
In the folder backend run:
```
docker-compose up
```

PhpMyAdmin Port:8081

### Manual, after truncate all data

In the file **backend/__init__.py**, change database information by your
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/company'
```

Then launch the following command:
```
python3 create_data.py
```

## Backend

```
git clone https://github.com/rg3915/flask-vuejs.git
cd flask-vuejs
python3 -m venv .venv
cd /backend
pip install -r requirements.txt
pip install pymysql
python run.py
```

Port : 5000.


## Front-end

```
cd /frontend
npm install
npm run dev
```

Port : 8080.
