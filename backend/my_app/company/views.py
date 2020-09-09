from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.company.models import Company

company = Blueprint('company', __name__)


@company.route('/')
@company.route('/home')
def home():
    return "Welcome to the company Home."


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
        company = Company(siren, denomination, region, ville, code_postal, num_dept, date_immatriculation)
        db.session.add(company)
        db.session.commit()
        company_dict = {
            company.id: {
                'siren': company.siren,
                'denomination': company.denomination,
                'region': company.region,
                'ville': company.ville,
                'code_postal': company.code_postal,
                'num_dept': company.num_dept,
                'date_immatriculation': company.date_immatriculation
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
                    'date_immatriculation': company.date_immatriculation
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
                'date_immatriculation': company.date_immatriculation
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
        company = Company(siren, denomination, region, ville, code_postal, num_dept, date_immatriculation)
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
            'date_immatriculation': company.date_immatriculation
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

app.add_url_rule(
    '/company/',
    view_func=company_view,
    methods=['GET', 'POST']
)


app.add_url_rule(
    '/company/<int:id>',
    view_func=company_view,
    methods=['GET', 'DELETE']
)
