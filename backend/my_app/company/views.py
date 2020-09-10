from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.company.models import Company
from sqlalchemy import text

company = Blueprint('company', __name__)


@company.route('/')
@company.route('/home')
def home():
    return "Welcome to the company Home."

class CompanyCountCodeApe(MethodView):
    def get(self):
        mylist = []
        newList = []
        sql = text('select code_ape, count(code_ape) as c from company group by code_ape order by c DESC limit 51')
        result = db.engine.execute(sql)
        for row in result:
            if row[0] != '0000Z':
                mylist.append(row[0])
                newList.append(row[1])
        resultTab = [mylist,newList]
        return jsonify(resultTab)

class CompanyViewRequests(MethodView):
    '''
    CompanyView to use with requests.
    '''

    def post(self):
        data = request.form
        siren = data.get('siren')
        denomination = data.get('denomination')
        region = data.get('region')
        ville = data.get('ville')
        code_postal = data.get('code_postal')
        num_dept = data.get('num_dept')
        date_immatriculation = data.get('date_immatriculation')
        code_ape = data.get('code_ape')
        fiche_identite = data.get('fiche_identite')
        company = Company(siren, denomination, region, ville, code_postal, num_dept, date_immatriculation, code_ape, fiche_identite)
        db.session.add(company)
        db.session.commit()
        Company.query()
        company_dict = {
            company.id: {
                'siren': company.siren,
                'denomination': company.denomination,
                'region': company.region,
                'ville': company.ville,
                'code_postal': company.code_postal,
                'num_dept': company.num_dept,
                'date_immatriculation': company.date_immatriculation,
                'code_ape': company.code_ape,
                'fiche_identite': company.fiche_identite
            }
        }
        return jsonify(company_dict)


class CompanyView(MethodView):

    def get(self, id=None, page=1):
        _list = []
        if not id:
            companys = Company.query.paginate(page, 10000).items
            for company in companys:
                company_dict = {
                    'id': company.id,
                    'siren': company.siren,
                    'denomination': company.denomination,
                    'region': company.region,
                    'ville': company.ville,
                    'code_postal': company.code_postal,
                    'num_dept': company.num_dept,
                    'date_immatriculation': company.date_immatriculation,
                    'code_ape': company.code_ape,
                    'fiche_identite': company.fiche_identite
                }
                _list.append(company_dict)
        else:
            company = Company.query.filter_by(id=id).first()
            if not company:
                abort(404)
            company_dict = {
                'id': company.id,
                'siren': company.siren,
                'denomination': company.denomination,
                'region': company.region,
                'ville': company.ville,
                'code_postal': company.code_postal,
                'num_dept': company.num_dept,
                'date_immatriculation': company.date_immatriculation,
                'code_ape': company.code_ape,
                'fiche_identite': company.fiche_identite
            }
            _list.append(company_dict)
        data = {'data': _list}
        return jsonify(data)

    def post(self):
        data = request.get_json(force=True)
        siren = data.get('siren')
        denomination = data.get('denomination')
        region = data.get('region')
        ville = data.get('ville')
        code_postal = data.get('code_postal')
        num_dept = data.get('num_dept')
        date_immatriculation = data.get('date_immatriculation')
        code_ape = data.get('code_ape')
        fiche_identite = data.get('fiche_identite')
        company = Company(siren, denomination, region, ville, code_postal, num_dept, date_immatriculation, code_ape, fiche_identite)
        db.session.add(company)
        db.session.commit()
        company_dict = {
            'id': company.id,
            'siren': company.siren,
            'denomination': company.denomination,
            'region': company.region,
            'ville': company.ville,
            'code_postal': company.code_postal,
            'num_dept': company.num_dept,
            'date_immatriculation': company.date_immatriculation,
            'code_ape': company.code_ape,
            'fiche_identite': company.fiche_identite
        }
        data = {'data': company_dict}
        return jsonify(data)

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        company = Company.query.filter_by(id=id).first()
        db.session.delete(company)
        db.session.commit()
        response = {'message': 'Success'}
        return jsonify(response)


company_view_requests = CompanyViewRequests.as_view('company_view_requests')
company_view = CompanyView.as_view('company_view')
company_count_ape_view = CompanyCountCodeApe.as_view('company_count_ape_view')

app.add_url_rule(
    '/company/',
    view_func=company_view,
    methods=['GET', 'POST']
)

app.add_url_rule(
    '/company/count/',
    view_func=company_count_ape_view,
    methods=['GET']
)

app.add_url_rule(
    '/company/<int:id>',
    view_func=company_view,
    methods=['GET', 'DELETE']
)
