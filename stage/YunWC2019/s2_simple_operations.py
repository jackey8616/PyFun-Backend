from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/simple_operations',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Simple Operations',
    'author': 'Official',
    'description': [
        'This time let\'s calculate some math!',
        'Try to fill the blank and output with 3, 5.0 and 16.',
        '數學時間！',
        '填滿空格, 輸出3, 5.0 跟 16！'
    ],
    'code': [
        'print(1+4_____)',
        'print(10_____)',
        'print(_____5+3_____*2)'
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
            ans = ['3', '5.0', '16']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
