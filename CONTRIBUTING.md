
# Contributing new stage or lession

Inside `stage` module.  
There is two sub-module named `one` and `two`.  
Each sub-module folder should contains `__init__.py` for auto import.  

## Creating a new stage
Inside `stage` folder, `mkdir` a new stage with name you want.  
And create a mininum `__init__.py` with following `dict`:  
```python
setup = {
  'path': 'path/to/sub-module', # This str will be use in os.path.join(), Do NOT starts with /
  'url': '/stage/one/',         # index url for stage page. Will be DEPRECATED soon.
  'package': 'stage.one'        # Package path to sub-module, use for __import__ function call.
}
```

## Creating a new lession
Inside the `stage/[stage_name]` folder (such as `stage/one`).  
Make sure there is a mininum `__init__.py`.  


And create new file with any name you like ,
But file name show same as function name.  
**IMPORTANT**
```
If you wish your lessions can be sort.
Naming these lession file can use some count such as:
Example:
  You have a lession want to called i_love_haruna, and you wish it in place 35
  Then you shoud create a file called s35_i_love_haruna.py with a async function like:
  async def i_love_haruna(request):
```
With following code:  
```python
import traceback
from sanic.response import json

from utils import fields_generate, concat_code
from utils import file_generate, file_execute

# YOU SHOULD PROPERLY EDIT FEW SECTION:
# route:       dict for good Sanic route setup and auto import.
# data:        dict for present at Frontend
# answer:      function is to judge stdout result is correct or wrong.
#              This must be manually write in order to judge.

route = {
    'function': 'hello_python',       # Async def function name below.
    'url': '/stage/one/hello_python', # Url for Sanic to set route.
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Hello Python',  # Any title would show in Frontend.
    # image is optional, suggest use https
    'image': 'https://community-cdn-digitalocean-com.global.ssl.fastly.net/assets/tutorials/images/large/EBOOK_PYTHON_no-name.png?1516826609',
    'description': [
        'Hello there!',
        'I see that you are a new face!',
        'Try to say Hello to me!'
    ],
    # code with a array, each blank show with five underline(_),
    # fronend will automatically translate to <input> tag.
    # remember each line should escape with special character.
    'code': [
        '_____(\'_____\')'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)  # NEVER remove this line!!

async def hello_python(request):
    try:
        if request.method == 'GET':
            global data
            return json({ 'success': True, 'data': data })
        else:
            code_data = concat_code(data, request.json)
            file_name = file_generate(code_data)
            stdout, stderr = file_execute(file_name)
            result = answer(stdout, stderr)
            return json({ 'success': True, 'data': { 'result': result, 'stdout': stdout, 'stderr': stderr} })
    except:
        return json({ 'fail': True, 'error': traceback.format_exc() })

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0].decode() == 'Hello Python\n'
    except:
        return False
```
