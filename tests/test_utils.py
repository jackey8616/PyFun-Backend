
from utils import fields_generate, concat_code, get_import_dirs


def test_fields_generate():
    data = {
        'code': [ '_____', '_____' ]
    }

    assert fields_generate(data) == [ 'field_1', 'field_2' ] 

def test_concat_code():
    data = {
        'code': [ '_____', '_____' ]
    }
    data['fields'] = fields_generate(data)
    form = {
        'field_1': '123',
        'field_2': '456'
    }
    assert concat_code(data, form) == '123\n456\n'
    
def test_get_import_dirs():
    pass

