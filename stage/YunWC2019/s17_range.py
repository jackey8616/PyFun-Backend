from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/range',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Range',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '[0, 1, 2, 3, 4]', '[6, 7, 8, 9, 10]', '[10, 8, 6, 4, 2]'
    ],
    'code': [
        'print(list(range(_____)))',
        'print(list(range(_____, _____)))',
        'print(list(range(_____, _____, _____)))'
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
            ans = ['[0, 1, 2, 3, 4]', '[6, 7, 8, 9, 10]', '[10, 8, 6, 4, 2]']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
