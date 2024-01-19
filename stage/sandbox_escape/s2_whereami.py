from os import getcwd

from utils.form import blank_form

route = {
    'type': blank_form,
    'url': '/stage/sandbox_escape/whereami',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'whereami',
    'author': 'Official',
    'description': [
        'Whereami?',
        '我在哪？'
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
            return stdout[0] == "{}\n".format(getcwd())
    except Exception:
        return False
