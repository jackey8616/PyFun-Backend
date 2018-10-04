import traceback
from sanic.response import json

from utils import get_import_files, import_files
from utils import get_import_dirs, import_dirs, list_paths


pys = get_import_dirs('stage')
imports = import_dirs(pys, globals(), locals(), 'stage')


async def index(request):
    stages = {}
    global imports
    for (key, module) in imports.items():
        setup = getattr(module, 'setup')
        module_pys = get_import_files(setup['path'])
        stages[key] = list_paths(module_pys)
    return json({'success': True, 'data': stages})


def add_route(app):
    app.add_route(index, '/stage/', methods=['GET'])
    global imports
    for (key, module) in imports.items():
        setup = getattr(module, 'setup')
        module_pys = get_import_files(setup['path'])
        module_imports = import_files(module_pys, globals(), locals(),
                                      setup['package'])
        for (key, value) in module_imports.items():
            route = value.route
            app.add_route(getattr(value, 'sanic_request'), route['url'],
                          route['methods'])
