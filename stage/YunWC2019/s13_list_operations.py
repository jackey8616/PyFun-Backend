from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/list_operations',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'List Operations',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '[4, 5, 6, 7, 8, 9]', '[4, 5, 6, 4, 5, 6]', '8'
    ],
    'code': [
        'numbers = [4, 5, 6]',
        'print(numbers + _____)',
        'print(numbers * _____)',
        '',
        'numbers[1] = numbers[_____] + 2',
        'print(numbers[1])'
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
            ans = ['[4, 5, 6, 7, 8, 9]', '[4, 5, 6, 4, 5, 6]', '8']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
