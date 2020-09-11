# Project flask end VueJS

Flask api Rest and VueJS.

## Download Project
```
git clone git@github.com:mparis98/Data-Python.git
cd Data-Python
```

## Initialize BDD

### Automatic (creat also creat database with value)
In the folder backend run:
```
docker-compose up
```

## Manual

### Backend

```
python3 -m venv .venv
cd backend/
pip install -r requirements.txt
pip install pymysql
```
If **python** doesn't work, please try **python3**
If **pip** doesn't work, please try **pip3**

In the file **backend/__init__.py**, change database information by your
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/company'
```

And **run** the backend :
```
python run.py
```

Url : http://localhost:5000

Then launch the following command:
```
python3 create_data.py
```

### Front-end

```
cd frontend/
npm install
npm run dev
```

Url : http://localhost:8080.
