
import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

route = {
    'function': 'if_elif_else',
    'url': '/stage/one/if_elif_else',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'If ElseIf and Else',
    'image': 'https://myanimelist.cdn-dena.com/images/characters/6/276027.jpg',
    'description': [
        'Do you know Haruna?',
        'If you know her, then you are my friend.'
    ],
    'code': [      
        'answer = _____',
        'if answer == \'I know her\':',
        '    print(\'We are best friend.\')',
        'elif answer == \'Who is she?\':',
        '    print(\'You are not my friend! go away!\')',
        'else:',
        '    print(\'May be you can understand who she is right now.\')'
        ],
    'fields': []
}
data['fields'] = fields_generate(data)

async def if_elif_else(request):
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
            return True
    except:
        return True

