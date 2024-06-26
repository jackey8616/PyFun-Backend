from base64 import b64encode
from json import dumps, loads
from traceback import format_exc

from manager import StageManager
from utils import (
    fields_generate,
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


def wrap_api_gateway_response(data):
    return {
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Origin',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': b64encode(dumps(data).encode('utf-8')),
    }


def stages_info_handler(event, context):
    stages = {}
    global imports
    for (key, module) in imports.items():
        setup = getattr(module, 'setup')
        stages[key] = {
            'index': setup['index'],
            'url': setup['url']
        }
    return wrap_api_gateway_response({'success': True, 'data': stages})


def stage_info_handler(event, context):
    stage_name = event['pathParameters']['stage_name']

    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    global imports, module_pys

    if stage_name not in stages and stage_name not in imports:
        return wrap_api_gateway_response({'fail': True, 'error': 'No suck stage'})

    lessons = {}
    for (lesson_key, lesson) in stages[stage_name].get_lessons().items():
        lessons[lesson_key] = {
            'index': lesson.index,
            'title': lesson.title,
            'url': lesson.setup.url,
        }
    
    if stage_name in imports:
        for (lesson_key, lesson_meta) in list_paths(module_imports[stage_name]).items():
            lessons[lesson_key] = lesson_meta

    return wrap_api_gateway_response({'success': True, 'data': lessons})


def lesson_info_handler(event, context):
    stage_name = event['pathParameters']['stage_name']
    lesson_name = event['pathParameters']['lesson_name']

    global module_imports
    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    if (stage_name not in stages and stage_name not in module_imports):
        return wrap_api_gateway_response({'fail': True, 'data': 'No such stage'})


    if (stage_name in stages):
        lessons = stages[stage_name].get_lessons()
        if (lesson_name in lessons):
            lesson = lessons[lesson_name]
            return wrap_api_gateway_response({'success': True, 'data': lesson.get_router_data()})

    if (stage_name in module_imports):
        lessons = module_imports[stage_name]
        if (lesson_name in lessons):
            lesson = lessons[lesson_name]
            lesson.data['fields'] = fields_generate(lesson.data)
            return wrap_api_gateway_response({'success': True, 'data': lesson.data})

    return wrap_api_gateway_response({'fail': True, 'data': 'No such lesson'})


def lesson_verify_handler(event, context):
    stage_name = event['pathParameters']['stage_name']
    lesson_name = event['pathParameters']['lesson_name']
    answer = loads(event['body'])['answer']

    global module_imports
    stage_manager = StageManager().build_from_static()
    stages = stage_manager.get_stages()
    if (stage_name not in stages and stage_name not in module_imports):
        return wrap_api_gateway_response({'fail': True, 'data': 'No such stage'})

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
        return wrap_api_gateway_response({'fail': True, 'data': 'No such lesson'})

    try:
        code_data = concat_code(data, answer)
        stdout, stderr = data_execute(code_data)
        result = answer_func(stdout=stdout, stderr=stderr)
        return wrap_api_gateway_response({
            'success': True,
            'data': {
                'result': result,
                'stdout': stdout,
                'stderr': stderr,
            }
        })
    except Exception:
        return wrap_api_gateway_response({'fail': True, 'error': format_exc()})

