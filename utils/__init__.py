
import os, time
from subprocess import Popen, PIPE
from hashlib import md5

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

