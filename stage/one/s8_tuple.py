from utils.form import blank_form
from utils import fields_generate

route = {
    'type': blank_form,
    'url': '/stage/one/tuple',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Introduction to Tuple',
    'description': [
        'Hello there!',
        "Let's get started with tuples",
        'Try to print a tuple with me'
    ],
    'code': [
        'a=(1,"x","TUPLE")',
        'print(a)'
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
            return stdout[0].decode() == "(1,'x','TUPLE')\n"
    except:
        return False
