from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/type_conversion',
    'methods': ['GET', 'POST']
}

data = {
    'title': '',
    'author': 'Official',
    'description': [
        'Happy New Year!',
        'Here is some number, can you give me some integer ',
        ' and say 2019 Happy New Year to me?',
        '# print out "123456" and "2019 Happy New Year"',
        '新的一年來了, 你能夠幫我把一些礙眼的小數點給變不見嗎？',
        '印出"123456"跟"2019 Happy New Year"吧！'
    ],
    'code': [
        'print(_____1234.56_____)',
        'print(_____2019_____ + " Happy New Year")'
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
            ans = ["1234", "2019 Happy New Year"]
            for each in range(0, len(ans)):
                if stdout[each].decode() != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
