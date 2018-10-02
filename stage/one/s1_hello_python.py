
import traceback
from sanic.response import json

from utils import file_generate, file_execute

route = {
    'function': 'hello_python',
    'url': '/stage/one/hello_python',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Hello Python',
    'image': 'https://community-cdn-digitalocean-com.global.ssl.fastly.net/assets/tutorials/images/large/EBOOK_PYTHON_no-name.png?1516826609',
    'description': [
        'Hello there!',
        'I see that you are a new face!',
        'Try to say Hello to me!'
    ],
    'code': [
        '_____(\'_____\')'
    ],
    'fields': [
        'field_1',
        'field_2'
    ]
}

async def hello_python(request):
    try:
        if request.method == 'GET':
            global data
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr} })
    except:
        return json({ 'fail': True, 'error': traceback.format_exc() })

# Q1: Hello Python
# _____('_______')
# Under python3, please print Hello Python.
# A1: print('Hello World')
def concat_code(form):
    return "{0}('{1}')".format(
        form['field_1'] if 'field_1' in form else '', 
        form['field_2'] if 'field_2' in form else '')

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0].decode() == 'Hello Python\n'
    except:
        return False

