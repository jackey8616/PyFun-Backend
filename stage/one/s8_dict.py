from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/dict',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Dictionaries',
    'author': 'vincentt117',
    'image': 'https://community-cdn-digitalocean-com.global.ssl.fastly.net/' +
             'assets/tutorials/images/large/' +
             'EBOOK_PYTHON_no-name.png?1516826609',
    'description': [
        'Lets get familiar with Python diciontaries (dict).',
        'In Python, dictionary is a collection of key value pairs, ' +
        'such that each key of a given type maps to a value of a given type.',
        'You can reference dictionary methods here: https://docs.python.org/' +
        '3/tutorial/datastructures.html#dictionaries',
        '\n',
        'Now lets work on some exercises. You have a following ' +
        'array of integers: [1, 1, 2, 1, 1, 2, 2]',
        'Use a dictionary to count the frequency of each element ' +
        'do not use any other data structures.'
    ],
    'code': [
        'l = [1, 1, 2, 1, 1, 2, 2]',
        'counter = {}',
        'for i in l:',
        '    if i in counter:',
        '        _____[i] += 1',
        '    else:',
        '        _____[i] = 1',
        'print(str(counter))'
    ]
}


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans1 = {1: 4, 2: 3}
            ans2 = {2: 3, 1: 4}
            return stdout[0] == str(ans1) + "\n" or \
                stdout[0] == str(ans2) + "\n"
    except Exception:
        return False
