
from utils.form import blank_form
from utils import fields_generate

route = {
    'type': blank_form,
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

async def sanic_request(request):
    try:
        return override(request)
    except NameError:
        global data, route
        return route['type'](data, request, answer)

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

