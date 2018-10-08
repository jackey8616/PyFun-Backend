import time

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
    data['fields'] = fields_generate(data)
    form = {
        'field_1': '123',
        'field_2': '456'
    }
    assert concat_code(data, form) == '123\n456\n'


def test_get_import_dirs():
    pass


def test_list_paths():
    pys = {
        'hello_python': __import__('stage.one.s1_hello_python', {}, {},
                                   ['__file__', 'route', 'data'])
    }
    out = list_paths(pys=pys)
    assert out['hello_python']['index'] == '1'
    assert out['hello_python']['title'] == pys['hello_python'].data['title']
    assert out['hello_python']['url'] == pys['hello_python'].route['url']


def test_md5_content():
    md5 = __import__('hashlib').md5()
    t = time.time()
    data = 'abc'
    out = md5.update((str(t) + data).encode('utf-8'))
