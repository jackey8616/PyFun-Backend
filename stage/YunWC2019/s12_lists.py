from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/lists',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Lists',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '3', '9', '1', '[3, 6, 9, 1, 5]'
    ],
    'code': [
        'numbers = [3, 6, 9, 1, 5]',
        'print(numbers[_____])',
        'print(numbers[_____])',
        'print(numbers[-_____])',
        'print(_____)'
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
            ans = ['3', '9', '1', '[3, 6, 9, 1, 5]']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
