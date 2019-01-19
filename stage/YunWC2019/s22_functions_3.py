from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/functions_3',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Functions (3)',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '75'
    ],
    'code': [
        'def sum(numbers):',
        '    s = 0',
        '    for n in _____:',
        '        s _____ n',
        '',
        '    return _____',
        '',
        'def average(numbers):',
        '    return sum(numbers) / _____(numbers)',
        '',
        'print(int(average([60, 90, 70, 80])))'
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
            ans = ['75']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
