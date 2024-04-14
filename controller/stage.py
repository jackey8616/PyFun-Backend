from __future__ import annotations

from sanic import Blueprint
from sanic.response import json

from utils import get_import_files, get_import_dirs, import_files, import_dirs, list_paths

stage_blueprint = Blueprint('stage', url_prefix='stage')

pys = get_import_dirs('stage')
imports = import_dirs(pys, globals(), locals(), 'stage')
module_imports = {}
module_pys = {}

@stage_blueprint.route('', methods=['GET'])
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

@stage_blueprint.route('<stage_name>', methods=['GET'])
async def stage_index(request, stage_name: str):
    lessons = {}
    global imports, module_pys
    if stage_name in imports:
        lessons = list_paths(module_imports[stage_name])
        return json({'success': True, 'data': lessons})
    else:
        return json({'fail': True, 'error': 'No suck stage.'})


def construct_sanic_request(override, data, route, answer):
    async def sanic_request(request):
        if override:
            return override(request)
        else:
            return route['type'](data, request, answer)
    
    return sanic_request

def add_route_by_imports(blueprint):
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
            blueprint.add_route(
                handler=construct_sanic_request(
                    override=getattr(value, 'override') if hasattr(value, 'override') else None,
                    data=value.data,
                    route=route,
                    answer=value.answer,
                ),
                name=routeName,
                uri=route['url'].replace('/stage', '', 1),
                methods=route['methods'],
            )
