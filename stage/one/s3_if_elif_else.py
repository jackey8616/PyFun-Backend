from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/if_elif_else',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'If ElseIf and Else',
    'author': 'Official',
    'image': 'https://myanimelist.cdn-dena.com/images/characters/6/276027.jpg',
    'description': [
        'Do you know Haruna?',
        'If you know her, then you are my friend.'
    ],
    'code': [
        'answer = _____',
        'if answer == \'I know her\':',
        '    print(\'We are best friend.\')',
        'elif answer == \'Who is she?\':',
        '    print(\'You are not my friend! go away!\')',
        'else:',
        '    print(\'May be you can understand who she is right now.\')'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return True
    except Exception:
        return True
