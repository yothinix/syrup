from datetime import datetime

from sanic import Sanic
from sanic_openapi import swagger_blueprint, openapi_blueprint

from views import account, transaction, transaction_instance

app = Sanic()

app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

app.add_route(transaction, '/transaction/', methods=['GET', 'PATCH', 'POST'])
app.add_route(transaction_instance, '/transaction/<pk:int>/', methods=['GET', 'PUT', 'DELETE'])
app.add_route(account, '/account/', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
