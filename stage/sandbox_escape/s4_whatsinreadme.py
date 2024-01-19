from os import system

from utils.form import blank_form

route = {
    'type': blank_form,
    'url': '/stage/sandbox_escape/whatsinreadme',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'whats in README',
    'author': 'Official',
    'description': [
        'Whats in README?'
        'README裡有什麼？'
    ],
    'code': [
        '_____("Ha Ha Ha'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0] == "{}\n".format(system("README.md"))
    except Exception:
        return False
