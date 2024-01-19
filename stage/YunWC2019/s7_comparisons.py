from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/comparisions',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Comparisons',
    'author': 'Official',
    'description': [
        'Who is bigger, and who is smaller?',
        'Show me the answers of these comparasions!',
        'Watch out the capital!',
        '比大小！',
        '告訴我這些判斷式的結果！',
        '別忘記字首大小寫喔！'
    ],
    'code': [
        '10 > 3',
        '13 <= 10 + 3',
        '16 == "16"',
        '6 != int("6")',
        'print(_____)',
        'print(_____)',
        'print(_____)',
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
            ans = ['True', 'True', 'False', 'False']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
