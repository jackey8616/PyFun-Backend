import os, time
from os import listdir
from os.path import isfile, isdir, join
from subprocess import Popen, PIPE
from hashlib import md5


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
    pys = [(f[f.index('_') + 1:-3], f) for f in ls_files if isfile(join(path, f)) and f != '__init__.py']
    return pys


def import_dirs(pys, _globals, _locals, path):
    imports = {}
    for each in pys:
        imports[each] = __import__(path + '.' + each, _globals, _locals, [each], 0)
    return imports


def import_files(pys, _globals, _locals, path):
    imports = {}
    for (module, file_name) in pys:
        imports[module] = __import__(path + '.' + file_name[:-3], _globals, _locals, [module], 0)
    return imports


def list_paths(pys):
    ls = []
    for (module, file_name) in pys:
        ls.append(module.replace('_', ' '))
    return ls


def md5_content(data):
    data = str(time.time()) + data
    hasher = md5()
    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest()


def file_generate(data):
    file_name = os.path.join(os.getcwd(), 'tmp/{0}.py'.format(md5_content(data)))
    with open(file_name, 'w') as py_file:
        py_file.write(data)
    return file_name


def file_execute(file_name):
    p = Popen(['python3', file_name], stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.stdout.readlines(), p.stderr.readlines()
    os.remove(file_name)
    return stdout, stderr
