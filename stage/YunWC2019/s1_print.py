from utils.form import blank_form


route = {
    'type': blank_form,
    'url': '/stage/YunWC2019/print',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Print',
    'author': 'Official',
    'description': [
        'Here is some blank fields.',
        'Can you help me to fill it, and make it print out "Ha Ha Ha~"?',
        '這邊有一些空白的欄位.',
        '你可以幫我填滿它們來輸出"Ha Ha Ha~"嗎？'
    ],
    'code': [
        '_____("Ha Ha Ha_____'
    ]
}



def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0] == 'Ha Ha Ha~\n'
    except Exception:
        return False
