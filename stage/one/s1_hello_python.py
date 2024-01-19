from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/one/hello_python',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Hello Python',
    'author': 'Official',
    'image': 'https://community-cdn-digitalocean-com.global.ssl.fastly.net/' +
             'assets/tutorials/images/large/' +
             'EBOOK_PYTHON_no-name.png?1516826609',
    'description': [
        'Hello there!',
        'I see that you are a new face!',
        'Try to say Hello to me!'
    ],
    'code': [
        '_____(\'_____\')'
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
            return stdout[0] == 'Hello Python\n'
    except Exception:
        return False
