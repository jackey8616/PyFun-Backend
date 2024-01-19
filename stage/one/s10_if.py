from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/if',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'If',
    'author': 'claudiavmbrito',
    'description': [
        'Lets get familiar with Python If-Conditions!',
        'As the name indicates, If-conditions work as ' +
        'they are named, "If something happened, then something else happens".',
        'You can reference if statements here: https://docs.python.org/3/' +
        'tutorial/controlflow.html',
        '\n',
        'Now lets work on some exercises. A person is 20 year old age ' +
        'is she young or old?',
        'Create a if statement that prints that if a person is older than ' +
        '18 years old is old, otherwise the person is young.'
    ],
    'code': [
        'age = 20',
        'if (_____):',
        '    print(\'You are old\')',
        'else:',
        '    print(\'You are young\')',
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = "You are old\n"
            if stdout[0] != ans:
                return False
            return True
    except Exception:
        return False
