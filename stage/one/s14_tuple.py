from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/tuples',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Tuples',
    'description': [
        'Lets get familiar with Python tuples.',
        'A tuple is a collection which is ordered and unchangeable.',
        'You can find more information about tuples here: ',
        'https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences',
        'You can create a tuple using several ways, as example - to use tuple() function.',
        'Now you have an array of numbers: [1, 2, 3, 4, 5].',
        'Lets transform it into a tuple and then create another tuple',
        'with additional element which is 0.'
    ],
    'code': [
        'l = [1, 2, 3, 4, 5]',
        'tuple_1 = _____(l)',
        'tuple_2 = _____, _____',
        'print(str(tuple_2))'
    ]
}


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0] == "(0, (1, 2, 3, 4, 5))\n"
    except Exception:
        return False
