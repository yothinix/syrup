from datetime import datetime

from sanic import Sanic
from sanic_openapi import swagger_blueprint, openapi_blueprint

from views import account, transaction, transaction_instance

app = Sanic()

app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

app.config.API_VERSION = '1.0.0'
app.config.API_TITLE = 'Syrup API'
app.config.API_DESCRIPTION = 'An API for Syrup money application'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
app.config.API_CONTACT_EMAIL = 'm@yothinix.com'

app.add_route(transaction, '/transaction/', methods=['GET', 'PATCH', 'POST'])
#app.add_route(transaction_instance, '/transaction/<pk:int>/', methods=['GET', 'PUT', 'DELETE'])
#app.add_route(account, '/account/', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
