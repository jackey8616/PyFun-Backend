from utils.form import blank_form
from utils import fields_generate

route = {
    'type': blank_form,
    'url': '/stage/one/list',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'List',
    #'image': 'https://community-cdn-digitalocean-com.global.ssl.fastly.net/assets/tutorials/images/large/EBOOK_PYTHON_no-name.png?1516826609',
    'description': [
        'Hello there!',
        'Lets start with lists!',
        'Try to print an list with different data types'
    ],
    'code': [
        'Lst = [1, "a" , "string"]', 
        'print(Lst)'
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
            return stdout[0].decode() == '[1, 'a', 'string']\n'
    except:
        return False
