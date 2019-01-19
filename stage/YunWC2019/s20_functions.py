from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/functions',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Functions',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        'Hi'
    ],
    'code': [
        '_____ hello() _____',
        '    print(\'Hi\')',
        '',
        '_____()'
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
            ans = ['Hi']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
