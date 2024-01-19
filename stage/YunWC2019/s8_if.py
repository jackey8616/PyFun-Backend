from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/if',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'If',
    'author': 'Official',
    'description': [
        'Here is some decisions need to make.',
        'Can you let all of these results be Good?',
        '學會決策！',
        '填滿空格, 我想看到"Good!"的結果！'
    ],
    'code': [
        'num = _____',
        '',
        'if num > 7:',
        '    if num % 3 == 0:',
        '        print("Good!")',
        '',
        'text = _____',
        '',
        'if text != "Good!":',
        '    print("Bad!")',
        'else:',
        '    print("Good!")',
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
            ans = ['Good!', 'Good!']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
