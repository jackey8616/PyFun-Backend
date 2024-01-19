from sanic import Sanic, Blueprint
from sanic.response import json

from utils import get_import_files, import_files
from utils import get_import_dirs, import_dirs, list_paths

stageBp = Blueprint('stage', url_prefix='stage')

pys = get_import_dirs('stage')
imports = import_dirs(pys, globals(), locals(), 'stage')
module_pys = {}
module_imports = {}

@stageBp.route('', methods=['GET'])
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

@stageBp.route('<stage_name>', methods=['GET'])
async def stage_index(request, stage_name: str):
    lessons = {}
    global imports, module_pys
    if stage_name in imports:
        lessons = list_paths(module_imports[stage_name])
        return json({'success': True, 'data': lessons})
    else:
        return json({'fail': True, 'error': 'No such stage.'})


def add_route():
    global imports, module_pys, module_imports
    for (stageKey, module) in imports.items():
        setup = getattr(module, 'setup')
        module_pys[stageKey] = get_import_files(setup['path'])
        module_imports[stageKey] = import_files(
            module_pys[stageKey],
            globals(),
            locals(),
            setup['package'],
        )

        for (lessonKey, value) in module_imports[stageKey].items():
            route = value.route
            routeName = '{}_{}'.format(stageKey, lessonKey)
            stageBp.add_route(
                handler=getattr(value, 'sanic_request'),
                name=routeName,
                uri=route['url'].replace('/stage', '', 1),
                methods=route['methods'],
            )
