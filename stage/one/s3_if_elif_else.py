
import traceback
from sanic.response import json

from utils import file_generate, file_execute

async def if_elif_else(request):
    try:
        if request.method == 'GET':
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
                'fields': [ 'filed_1' ]
            }
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr} })
    except:
        return json({ 'fail': True, 'error': traceback.format_exc() })

# Q3: if elif else
# answer = _____
# if answer == 'I know her':
#     print('We are best friend.')
# elif answer == 'Who is she?':
#     print('You are not my friend! go away!')
# else:
#     print('May be you can understand who she is right now.')
def concat_code(form):
    return """
answer = '{0}'
if answer == 'I know her':
    print('We are best friend.')
elif answer == 'Who is she?':
    print('You are not my friend! go away!')
else:
    print('May be you can understand who she is right now.')
""".format(form['filed_1'] if 'filed_1' in form else '')

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return True
    except:
        return True

