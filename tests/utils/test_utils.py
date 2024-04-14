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
        'nested_for_loop': __import__('stage.one.s5_nested_for_loop', {}, {},
                                   ['__file__', 'route', 'data'])
    }
    out = list_paths(pys=pys)
    assert out['nested_for_loop']['index'] == '5'
    assert out['nested_for_loop']['title'] == pys['nested_for_loop'].data['title']
    assert out['nested_for_loop']['url'] == pys['nested_for_loop'].route['url']
