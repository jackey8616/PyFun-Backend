from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/for_loop',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'For Loop',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '1', '4', '7', '10'
    ],
    'code': [
        '_____ n _____ range(0, 10, _____):',
        '    print(_____ + 1)'
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
            ans = ['1', '4', '7', '10']
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
