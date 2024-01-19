from getpass import getuser

from utils.form import blank_form

route = {
    'type': blank_form,
    'url': '/stage/sandbox_escape/whoami',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'whoami',
    'author': 'Official',
    'description': [
        'Whoami?',
        '我是誰？'
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
            return stdout[0] == "{}\n".format(getuser())
    except Exception:
        return False
