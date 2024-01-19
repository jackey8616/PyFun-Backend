from os import listdir

from utils.form import blank_form

route = {
    'type': blank_form,
    'url': '/stage/sandbox_escape/whatsindir',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'whats in dir',
    'author': 'Official',
    'description': [
        'Whhats in dir?',
        '這裡有什麼？'
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
            return stdout[0] == "{}\n".format(listdir())
    except Exception:
        return False
