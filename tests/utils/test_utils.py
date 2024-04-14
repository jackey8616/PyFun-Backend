from utils import *


def test_fields_generate():
    data = {
        'code': ['_____', '_____']
    }

    assert fields_generate(data) == ['field_1', 'field_2']


def test_concat_code():
    data = {
        'code': ['_____', '_____']
    }
    form = {
        'field_1': '123',
        'field_2': '456'
    }
    assert concat_code(data, form) == '123\n456\n'


def test_get_import_dirs():
    pass


def test_list_paths():
    pys = {
        'basic_type': __import__('stage.one.s2_basic_type', {}, {},
                                   ['__file__', 'route', 'data'])
    }
    out = list_paths(pys=pys)
    assert out['basic_type']['index'] == '2'
    assert out['basic_type']['title'] == pys['basic_type'].data['title']
    assert out['basic_type']['url'] == pys['basic_type'].route['url']
