from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/basic_type',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Basic Type',
    'author': 'Official',
    'description': [
        'Here is some simple math,',
        'Can you help me to solve it?'
    ],
    'code': [
        'a = 10',
        'print(a == 10)',
        'b = _____',
        'print(a + b == 100)'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            for each in stdout:
                if each != 'True\n':
                    return False
            return True
    except Exception:
        return False
