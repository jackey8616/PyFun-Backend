from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/in_place_operators',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'In-Place Operators',
    'author': 'Official',
    'description': [
        'Add and equal, minus and equal.. ting~ ting~ ting~.',
        'Can you do some math and give me "13, 42, and 8.0"?',
        '加加減減程乘除除, 你能不能試著濃縮一些算式呢？',
        '請印出"13, 42, 跟 8.0"！'
    ],
    'code': [
        'x = 10',
        'x_____3',
        'print(x)',
        'x_____2',
        'print(x_____)',
        'x += 30',
        'x /= _____',
        'print(x)',
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
            ans = ['13', '42', '8.0']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
