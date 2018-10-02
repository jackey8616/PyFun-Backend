
import traceback
from sanic.response import json

from stage.one import add_route as one_add_route

async def index(request):
    stages = {
        'one': [
            'hello python',
            'basic type',
            'if elif else',
            'for loop',
            'for loop 2'
        ]
    }
    return json({ 'success': True, 'data': stages })

def add_route(app):
    app.add_route(index, '/stage/', methods=['GET'])
    one_add_route(app)
