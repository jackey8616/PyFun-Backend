
import traceback
from sanic.response import json

from utils import file_generate, file_execute

async def for_loop(request):
    try:
        if request.method == 'GET':
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
                'fields': [ 'field_1', 'field_2', 'field_3' ]
            }
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr }})
    except:
        return json({ 'fail': True, 'data': traceback.format_exc() })


# Q4
# for each in range(0, _____):
#     print(each + _____)
def concat_code(form):
    return """
for each in range({0}, {1}, {2}):
    print(each)
""".format(
    form['field_1'] if 'field_1' in form else '',
    form['field_2'] if 'field_2' in form else '',
    form['field_3'] if 'field_3' in form else '')

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
            
