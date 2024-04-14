from base64 import b64decode
from json import loads
from traceback import format_exc

from manager import StageManager
from utils import (
    concat_code,
    data_execute,
    get_import_files,
    get_import_dirs,
    import_files,
    import_dirs,
    list_paths,
)

pys = get_import_dirs('stage')
imports = import_dirs(pys, globals(), locals(), 'stage')
module_imports = {}
module_pys = {}
for (stageKey, module) in imports.items():
    setup = getattr(module, 'setup')
    module_pys[stageKey] = get_import_files(setup['path'])
    module_imports[stageKey] = import_files(
        module_pys[stageKey],
        globals(),
        locals(),
        setup['package'],
    )


def stages_info_handler(event, context):
    stages = {}
    global imports
    for (key, module) in imports.items():
        setup = getattr(module, 'setup')
        stages[key] = {
            'index': setup['index'],
            'url': setup['url']
        }
    return {'success': True, 'data': stages}


def stage_info_handler(event, context):
    stage_name = event['pathParameters']['stage_name']

    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    global imports, module_pys

    if stage_name not in stages and stage_name not in imports:
        return {'fail': True, 'error': 'No suck stage'}

    lessons = {}
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

    return {'success': True, 'data': lessons}


def lesson_info_handler(event, context):
    stage_name = event['pathParameters']['stage_name']
    lesson_name = event['pathParameters']['lesson_name']

    global module_imports
    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    if (stage_name not in stages and stage_name not in module_imports):
        return {'fail': True, 'data': 'No such stage'}


    if (stage_name in stages):
        lessons = stages[stage_name].get_lessons()
        if (lesson_name in lessons):
            lesson = lessons[lesson_name]
            return {'success': True, 'data': lesson.get_router_data()}

    if (stage_name in module_imports):
        lessons = module_imports[stage_name]
        if (lesson_name in lessons):
            lesson = lessons[lesson_name]
            return {'success': True, 'data': lesson.data}

    return {'fail': True, 'data': 'No such lesson'}


def lesson_verify_handler(event, context):
    stage_name = event['pathParameters']['stage_name']
    lesson_name = event['pathParameters']['lesson_name']
    answer = loads(b64decode(event['body']['answer']))

    global module_imports
    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    if (stage_name not in stages and stage_name not in module_imports):
        return {'fail': True, 'data': 'No such stage'}

    data, answer_func = None, None
    if (stage_name in stages):
        lessons = stages[stage_name].get_lessons()
        if (lesson_name in lessons):
            lesson = lessons[lesson_name]
            data, answer_func = lesson.get_router_data(), lesson.answer.verify_answer
    if (stage_name in module_imports):
        lessons = module_imports[stage_name]
        if (lesson_name in lessons):
            lesson = lessons[lesson_name]
            data, answer_func = lesson.data, lesson.answer
        
    if data is None:
        return {'fail': True, 'data': 'No such lesson'}

    try:
        code_data = concat_code(data, answer)
        stdout, stderr = data_execute(code_data)
        result = answer_func(stdout=stdout, stderr=stderr)
        return {
            'success': True,
            'data': {
                'result': result,
                'stdout': stdout,
                'stderr': stderr,
            }
        }
    except Exception:
        return {'fail': True, 'error': format_exc()}

