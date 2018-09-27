
import traceback
from sanic.response import json

from utils import file_generate, file_execute

async def basic_type(request):
    try:
        if request.method == 'GET':
            data = {
                'description': [
                    'Here is some simple math,',
                    'Can you help me to solve it?'
                ],
                'fields': [ 'filed_1', 'filed_2' ]
            }
            return json({ 'success': True, 'data': data })
        elif request.method == 'POST':
            code_data = concat_code(request.form)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr} })
    except:
        return json({ 'fail': True, 'error': traceback.format_exc() })

# Q2: Basic Type
# a = 10
# print(a == 10)
# b = ____
# print(a + b == 100)
# A2: 90
def concat_code(form):
    return """
a = 10
print(a == 10)
b = {0}
print(a + b == 100)
""".format(form['filed_1'][0])

def answer(stdout, stderr):
    if stderr != []:
        return False
    else:
        for each in stdout:
            if each.decode() != 'True\n':
                return False
        return True

