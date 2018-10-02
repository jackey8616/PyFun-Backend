
import os, time
from os import listdir
from os.path import isfile, join
from subprocess import Popen, PIPE
from hashlib import md5

def get_import_files(path):
    path = join(os.getcwd(), path)
    pys = [ (f[f.index('_') + 1:-3], f) for f in listdir(path) if isfile(join(path, f)) and f != '__init__.py']
    return pys

def import_files(pys, _globals, _locals, path):
    imports = {}
    for (module, file_name) in pys:
        imports[module] = __import__(path + '.' + file_name[:-3], _globals, _locals, [ module ], 0)
        sub = getattr(imports[module], module)
        _locals[module] = sub
    return imports

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

