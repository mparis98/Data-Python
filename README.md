# Project flask end VueJS

Flask api Rest and VueJS.

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

## Initialize BDD
In the file "backend/__init__.py", change your database information
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password%@localhost/database'

```
Then manually create your database and launch the following command:
```
python3 create_data.py

```

Port : 5000.

## Front-end

```
cd /frontend
npm install
npm run dev
```

Port : 8080.