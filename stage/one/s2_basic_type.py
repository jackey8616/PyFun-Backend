
import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

route = {
    'function': 'basic_type',
    'url': '/stage/one/basic_type',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Basic Type',
    'description': [
        'Here is some simple math,',
        'Can you help me to solve it?'
    ],
    'code': [
        'a = 10',
        'print(a == 10)',
        'b = _____',
        'print(a + b == 100)'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)

async def basic_type(request):
    try:
        if request.method == 'GET':
            global data
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(data, request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr} })
    except:
        return json({ 'fail': True, 'error': traceback.format_exc() })

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            for each in stdout:
                if each.decode() != 'True\n':
                    return False
            return True
    except:
        return False

