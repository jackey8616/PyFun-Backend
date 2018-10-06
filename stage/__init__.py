import traceback
from sanic.response import json

from utils import get_import_files, import_files
from utils import get_import_dirs, import_dirs, list_paths


pys = get_import_dirs('stage')
imports = import_dirs(pys, globals(), locals(), 'stage')
module_pys = {}
module_imports = {}

async def index(request):
    stages = {}
    global imports
    for (key, module) in imports.items():
        setup = getattr(module, 'setup')
        stages[key] = {
            'index': setup['index'],
            'url': setup['url']
        }
    return json({'success': True, 'data': stages})

async def stage_index(request, stage_name):
    lessons = {}
    global imports, module_pys
    if stage_name in imports:
        setup = getattr(imports[stage_name], 'setup')
        lessons = list_paths(module_imports[stage_name])
        return json({'success': True, 'data': lessons})
    else:
        return json({'fail': True, 'error': 'No such stage.'})


def add_route(app):
    app.add_route(index, '/stage/', methods=['GET'])
    app.add_route(stage_index, '/stage/<stage_name>', [ 'GET' ])
    global imports, module_pys, module_imports
    for (key, module) in imports.items():
        setup = getattr(module, 'setup')
        module_pys[key] = get_import_files(setup['path'])
        module_imports[key] = import_files(module_pys[key], globals(), locals(),
                                      setup['package'])
        for (key, value) in module_imports[key].items():
            route = value.route
            app.add_route(getattr(value, 'sanic_request'), route['url'],
                          route['methods'])
