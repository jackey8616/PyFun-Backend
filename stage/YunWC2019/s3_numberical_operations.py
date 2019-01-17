from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/numberical_operations',
    'methods': ['GET', 'POST']
}

data = {
    'title': '',
    'author': 'Official',
    'description': [
        'Here comes more advance caculations needs to complete.',
        'Try it! Fill it with answer 32, 3, and 4!',
        '又來了更多的運算啦！這次的更進階了,',
        '填滿它們！我想看到的答案有32, 3跟4!'
    ],
    'code': [
        'print(2_____5)',
        'print(20_____6)',
        'print(24_____5)'
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
            ans = ['32', '3', '4']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
