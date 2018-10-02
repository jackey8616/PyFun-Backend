
from sanic.response import json

from stage.one.s1_hello_python import hello_python
from stage.one.s2_basic_type import basic_type
from stage.one.s3_if_elif_else import if_elif_else
from stage.one.s4_for_loop import for_loop
from stage.one.s5_for_loop_2 import for_loop_2

async def index(request):
    return json({ 'success': True, 'data': 'Hello, here is stage one!' })

def add_route(app):
    app.add_route(index, '/stage/one/', methods=['GET'])
    app.add_route(hello_python, '/stage/one/hello_python', methods=['GET', 'POST'])
    app.add_route(basic_type, '/stage/one/basic_type', methods=['GET', 'POST'])
    app.add_route(if_elif_else, '/stage/one/if_elif_else', methods=['GET', 'POST'])
    app.add_route(for_loop, '/stage/one/for_loop', methods=['GET', 'POST'])
    app.add_route(for_loop_2, '/stage/one/for_loop_2', methods=['GET', 'POST'])

