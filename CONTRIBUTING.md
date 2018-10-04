
# Contributing new stage or lesson

Inside `stage` module.  
There is two sub-module named `one` and `two`.  
Each sub-module folder should contains `__init__.py` for auto import.  

## Creating a new stage
Inside `stage` folder, `mkdir` a new stage with name you want.  
And create a mininum `__init__.py` with following `dict`:  
```python
setup = {
  'path': 'backend/file/path/to/sub-module',   # This str will be use in os.path.join(), Do NOT starts with /
  'url': '/frontend/url/to/lesson',            # index url for stage page. Will be DEPRECATED soon.
  'package': 'package.to.sub-module'           # Package path to sub-module, use for __import__ function call.
}
```

## Creating a new lesson
Inside the `stage/[stage_name]` folder (such as `stage/one`).  
Make sure there is a mininum `__init__.py`.  


And create new file with any name you like ,
But file name show same as function name.  
**IMPORTANT**
```
If you wish your lessons can be sort.
Naming these lesson file can use some count such as:
Example:
  You have a lesson want to called i_love_haruna, and you wish it in place 35
  Then you shoud create a file called s35_i_love_haruna.py with a async function like:
  async def i_love_haruna(request):
```
With following code:  
```python
from utils.form import blank_form
from utils import fields_generate

# YOU SHOULD PROPERLY EDIT FEW SECTION:
# route:       dict for good Sanic route setup and auto import.
# data:        dict for present at Frontend
# answer:      function is to judge stdout result is correct or wrong.
#              This must be manually write in order to judge.

route = {
    'type': blank_form, # Right now only provide *blank_form* one kind of form 181004.
    'url': '/stage/one/hello_python',
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

async def sanic_request(request):
    try:
        return override(request)
    except NameError:
        global data, route
        return route['type'](data, request, answer)

# If you don't want to use any type of those.
# You can write yourself one, just properly handle Sanic request.
# **IMPORTANT** Unless you are sure to use customize one, or do not comment out this function.
# def override(request):
#     pass

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0].decode() == 'Hello Python\n'
    except:
        return False

```

## Provide a test
After you create a new lesson, you may wonder the code is function normal or not.  
Inside `tests/stage/[stage name]/` folder, create a new test py file starts with `test_`.
For example, `s1_hello_python.py` it's test file is `test_s1_hello_python.py`

Add following code:
```python
import json

async def test_hello_python(test_cli):
    # res = await test_cli.post('/replace/with/lesson/frontend/url/', data=json.dumps({ Here should be right answer's dictionary of your lesson, starts from field_1 to field_N }))
    # For exmaple, hello python have two field to fill in, so send a POST with {'field_1': 'print', 'field_2': 'Hello Python'} dict, the answer should be right, and result should be True
    res = await test_cli.post('/stage/one/hello_python', data=json.dumps({'field_1': 'print', 'field_2': 'Hello Python'}))
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] == True
    await test_cli.close()
```

Of course, If you want add more test to check your lesson is healthy, Just do it.  
Remember that make sure every sociate test should be in the same test file.
and every function should with `async`, `test_` prefix and only `test_cli` argument.

For example:
```python
# I want a new test function named haruna_cute
async def test_haruna_cute(test_cli):
    ...
    res = await test_cli.post('/replace/with/lesson/frontend/url/', data=json.dumps({ Data dictionary you want to test }))
    ...
```
