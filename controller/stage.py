from __future__ import annotations
from typing import Dict

from sanic import Blueprint
from sanic.response import json

from stage import Stage
from stage.lesson import Lesson
from manager import StageManager
from utils import get_import_files, get_import_dirs, import_files, import_dirs, list_paths
from utils.form import blank_form

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
    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    global imports, module_pys

    if stage_name not in stages and stage_name not in imports:
        return json({'fail': True, 'error': 'No such stage.'})

    lessons = {}
    if stage_name in stages:
        for (lesson_key, lesson) in stages[stage_name].get_lessons().items():
            index = lesson_key[1:lesson_key.index('_')]
            lessons[lesson_key.removeprefix('s{}_'.format(index))] = {
                'index': index, # should be int, wait for refactor
                'title': lesson.title,
                'url': lesson.setup.url,
            }

    if stage_name in imports:
        for (lesson_key, lesson_meta) in list_paths(module_imports[stage_name]).items():
            lessons[lesson_key] = lesson_meta

    return json({'success': True, 'data': lessons})


def construct_sanic_request(override, data, route, answer):
    async def sanic_request(request):
        if override:
            return override(request)
        else:
            return json(route['type'](data, request, answer))
    
    return sanic_request

def construct_sanic_request_kai(lesson: Lesson):
    async def sanic_request(request):
        return json(blank_form(lesson.get_router_data(), request, lesson.answer.verify_answer))
    
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

def add_route_by_stages(blueprint, stages: Dict[str, Stage]):
    for (stage_name, stage) in stages.items():
        for (lesson_name, lesson) in stage.get_lessons().items():
            blueprint.add_route(
                handler=construct_sanic_request_kai(lesson),
                name='{}/{}'.format(stage_name, lesson_name),
                uri=lesson.setup.url.replace('/stage', '', 1),
                methods=['GET', 'POST'],
            )
