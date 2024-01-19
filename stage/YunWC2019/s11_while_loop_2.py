from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/while_loop_2',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'While Loop (2)',
    'author': 'Official',
    'description': [
        'Print me the right answer with 4!',
        '正解是4，要怎麼填呢？'
    ],
    'code': [
        'num = 10',
        '',
        'while num > 0:',
        '    if _____:',
        '        break',
        '    num -= 2',
        '',
        'print(num)'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = ['4']
            for each in range(0, len(ans)):
                if stdout[each] != ans[each] + '\n':
                    return False
            return True
    except Exception:
        return False
