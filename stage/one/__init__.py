
from sanic.response import json
from stage.one.s1_hello_python import hello_python
from stage.one.s2_basic_type import basic_type

async def index(request):
    return json({ 'success': True, 'data': 'Hello, here is stage one!' })

def add_route(app):
    app.add_route(index, '/stage_one/', methods=['GET'])
    app.add_route(hello_python, '/stage_one/1_hello_python', methods=['GET', 'POST'])
    app.add_route(basic_type, '/stage_one/2_basic_type', methods=['GET', 'POST'])

