
import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

route = {
    'function': 'for_loop',
    'url': '/stage/one/for_loop',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'For Loop',
    'description': [
        'I like A.P. (Arithmetic Progression)',
        'Can you give me a A.P. with five numbers,',
        'And each difference is 2.'
    ],
    'code': [
        'for each in range(_____, _____, _____):',
        '    print(each)'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)

async def for_loop(request):
    try:
        if request.method == 'GET':
            global data
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(data, request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr }})
    except:
        return json({ 'fail': True, 'data': traceback.format_exc() })

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            if len(stdout) != 5:
                return False
            for each in range(1, len(stdout) - 1):
                if int(stdout[each]) - int(stdout[each - 1]) != 2:
                    return False
            return True
    except:
        return False
            
