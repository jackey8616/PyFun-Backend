from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/one/switch_case',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Switch Case',
    'author': 'b3_900d',
    'description': [
        'In other languages, it have switch case, python do not have it.\n',
        '  But we can use dict (in lession 8 ) for switch case condition'
    ],
    'code': [
        'kfc_menu = {}',
        'kfc_menu[\'burger\'] = 1000',
        'kfc_menu[\'pizza\'] = 2000',
        'kfc_menu[\'chicken\'] = 3000',
        'kfc_menu[\'drink\'] = 4000',
        'order = \'_____\'',
        'price = kfc_menu.get(order, "Oops not found")',
        'print(order, price)'
    ]
}


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0] in ["burger 1000\n",
                                          "pizza 2000\n",
                                          "chicken 3000\n",
                                          "drink 4000\n"]
    except Exception:
        return False
