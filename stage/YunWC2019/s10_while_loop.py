from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/while_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'While Loop',
    'author': 'Official',
    'description': [
        'Print me a result like below.',
        '填滿空格, 然後印出下列結果:',
        '5', '4', '3', '2', '1', '0', '10'
    ],
    'code': [
        'num = _____',
        '',
        '_____ num > 0:',
        '    num -= 1',
        '    print(num)',
        '',
        'print(num + _____)'
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
            ans = ['5', '4', '3', '2', '1', '0', '10']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
