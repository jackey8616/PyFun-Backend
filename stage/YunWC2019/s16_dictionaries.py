from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/dictionaries',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Dictionaries',
    'author': 'Official',
    'description': [
        'Print me the right answer like below:',
        '填滿空格, 然後印出下列結果:',
        '20', '1970/01/01'
    ],
    'code': [
        'man = _____\'name\': \'John\', \'age\': 20_____',
        'print(man[_____])',
        'man[\'birthday\'] = \'_____\'',
        'print(man[\'birthday\'])'
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
            ans = ['20', '1970/01/01']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
