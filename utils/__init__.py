import io
import os
from os import listdir
from os.path import isfile, isdir, join
import sys
import traceback


def fields_generate(data):
    fields = []
    count = 0
    for each in data['code']:
        count += each.count('_____')
    for each in range(1, count + 1):
        fields.append('field_{0}'.format(each))
    return fields


def concat_code(data, form):
    fields = data['fields']
    count = 0
    code = ''
    for each in data['code']:
        while each.count('_____') != 0:
            each = each.replace('_____', '{}', 1)
            each = each.format(form[fields[count]])
            count += 1
        code += each + '\n'
    return code


def get_import_dirs(path):
    path = join(os.getcwd(), path)
    ls_files = listdir(path)
    ls_files.sort()
    pys = [f for f in ls_files if isdir(join(path, f)) and f != '__pycache__']
    return pys


def get_import_files(path):
    path = join(os.getcwd(), path)
    ls_files = listdir(path)
    ls_files.sort()
    pys = []
    for f in ls_files:
        if isfile(join(path, f)) and f != '__init__.py':
            pys.append((f[f.index('_') + 1:-3], f))
    return pys


def import_dirs(pys, _globals, _locals, path):
    imports = {}
    for each in pys:
        imports[each] = __import__(path + '.' + each,
                                   _globals, _locals, [each], 0)
    return imports


def import_files(pys, _globals, _locals, path):
    imports = {}
    for (module, file_name) in pys:
        imports[module] = __import__(path + '.' + file_name[:-3],
                                     _globals, _locals, [module], 0)
    return imports


def list_paths(pys):
    ls = {}
    for (name, module) in pys.items():
        file_name = module.__file__[module.__file__.rfind('/') + 1:]
        index = ''
        for each in range(0, len(file_name) - 2):
            if file_name[each].isdigit():
                index += file_name[each]
            if file_name[each + 1] == '_':
                break
        ls[name] = {
            'index': index,
            'title': module.data['title'],
            'url': module.route['url']
        }
    return ls


def data_execute(data):
    captured_stdout = io.StringIO()
    captured_stderr = io.StringIO()
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr
    try:
        sys.stdout = captured_stdout
        sys.stderr = captured_stderr
        exec(data)
    except Exception:
        captured_stderr.write(traceback.format_exc())
    finally:
        sys.stdout = orig_stdout
        sys.stderr = orig_stderr

    # split into lines and encode() to preserve existing API
    def get_lines(sio):
        value = sio.getvalue()
        if not value:
            return []

        should_have_final_newline = False
        if value[-1] == '\n':
            should_have_final_newline = True
            value = value[:-1]

        lines = [(line + '\n').encode() for line in value.split('\n')]
        if not should_have_final_newline:
            lines[-1] = lines[-1][:-1]
        return lines

    return get_lines(captured_stdout), get_lines(captured_stderr)
