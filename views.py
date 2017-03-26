from datetime import datetime
import asyncio

import asyncpg
from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_openapi import doc


def mock_account_instance(name='test', amount=0):
    return {
        'name': name,
        'amount': amount
    }

def connectdb():
    return asyncpg.connect(user='postgres', password='postgres',
        database='syrup', host='localhost')

async def create_transaction(memo, amount, category):
    conn = await connectdb()
    results = await conn.fetch('''
        INSERT INTO transaction (memo, amount, category)
        VALUES ('{0}', {1}, '{2}');
    '''.format(memo, amount, category))
    await conn.close()

def transaction_serializer(instance):
    return {
        'id': instance['id'],
        'memo': instance['memo'],
        'amount': instance['amount'],
        'category': instance['category'],
        'timestamp': instance['timestamp'].isoformat(),
    }

class Transaction:
    memo = doc.String('Description for this transaction')
    amount = doc.Integer('A cost of this transaction')
    category = doc.String('Category for this transaction')

@doc.summary('Transactions API')
@doc.produces(Transaction)
async def transaction(request):
    if request.method == 'GET':
        conn = await connectdb()
        values = await conn.fetch('''
            SELECT * FROM transaction;
        ''')
        await conn.close()
        instances = []
        for instance in values:
            instances.append(transaction_serializer(instance))
        return json({
            'count': len(instances),
            'data': instances
        })

    elif request.method == 'POST':
        data = request.json
        await create_transaction(data['memo'], data['amount'], data['category'])
        return json({
            'count': 1,
            'message': 'added 1 transaction instance',
            'data': data
        })

    elif request.method == 'PATCH':
        for data in request.json:
            await create_transaction(data['memo'], data['amount'], data['category'])
        count = len(request.json)
        return json({
            'count': count,
            'message': 'added {0} transaction instance'.format(count),
            'data': request.json
        })


async def transaction_instance(request, pk):
    if request.method == 'GET':
        return json({'id': pk})
    elif request.method == 'PUT':
        return json({'id': pk})
    elif request.method == 'DELETE':
        return json({'id': pk})

async def account(request):
    if request.method == 'GET':
        return json(mock_account_instance('test_account', 12000))
    elif request.method == 'POST':
        return json({'created': True})

