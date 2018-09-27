
import traceback
from sanic.response import json

from utils import file_generate, file_execute

async def hello_python(request):
    try:
        if request.method == 'GET':
            data = {
                'description': [
                    'Hello there!',
                    'I see that you are a new face!',
                    'Try to say Hello to me!'
                ],
                'fields': [ 'filed_1', 'filed_2' ]
            }
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(request.form)
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
    return "{0}('{1}')".format(form['filed_1'][0], form['filed_2'][0])

def answer(stdout, stderr):
    if stderr != []:
        return False
    else:
        return stdout[0].decode() == 'Hello Python\n'

