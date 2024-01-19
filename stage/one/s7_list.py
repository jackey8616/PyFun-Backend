from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/list',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'List',
    'author': 'rozig',
    'description': [
        'Lets get familiar with Python list.',
        'In Python, list is a collection which is ordered and mutable ' +
        'sequence of objects.',
        'You can reference list methods here: https://docs.python.org/3/' +
        'tutorial/datastructures.html',
        '\n',
        'Now lets work on some exercises. You have a following ' +
        'list: [9, 1, 4, 7, 3, 0, 5]',
        'Sort the list first and then reverse it. You can\'t use sort with ' +
        'reverse argument.'
    ],
    'code': [
        'list_ = [9, 1, 4, 7, 3, 0, 5]',
        'list_._____()',
        'list_._____()',
        'print(str(list_))'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = "[9, 7, 5, 4, 3, 1, 0]\n"
            if stdout[0] != ans:
                return False
            return True
    except Exception:
        return False
