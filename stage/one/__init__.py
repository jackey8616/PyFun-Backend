
from sanic.response import json
from utils import get_import_files, import_files

pys = get_import_files('stage/one/')
imports = import_files(pys, globals(), locals(), 'stage.one')

async def index(request):
    return json({ 'success': True, 'data': 'Hello, here is stage one!' })

def add_route(app):
    app.add_route(index, '/stage/one/', methods=['GET'])
    global imports
    for (key, value) in imports.items():
        route = value.route
        app.add_route(getattr(value, route['function']), route['url'], route['methods'])

