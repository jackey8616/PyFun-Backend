
# Contributing new stage or lesson

Inside `stage` module.
There are currently two sub-modules named `one` and `two`.
Each sub-module folder should contain an `__init__.py` for auto import.

## Creating a new stage
Inside the `stage` folder, `mkdir` a new stage with a name you want.  
At minimum, you must create an `__init__.py` with following the `dict` to allow for auto import:  

```python
setup = {
  'index': 0,                                  # Stage index, can not duplicate, before setting, please check first.
  'path': 'backend/file/path/to/sub-module',   # This str will be use in os.path.join(), Do NOT start with /
  'url': '/frontend/url/to/lesson',            # index url for stage page. Will be DEPRECATED soon.
  'package': 'package.to.sub-module'           # Package path to sub-module, use for __import__ function call.
}
```

## Creating a new lesson

Inside the `stage/[stage_name]` folder (such as `stage/one`).  
Make sure there is a `__init__.py` file.  

Then, create a new file with an appropriate name to describe the lesson. Please see each each lessons's name
to get an idea of proper file naming convention. It is helpful if each file name describes the lesson's function name.  

**For Example:**
```
  You have a lesson you want to call i_love_haruna, and you want it to be the 35th lesson in the stage,
  Then you shoud create a file called s35_i_love_haruna.py with a async function like:
```

Follow the code structure below to set up your lesson!
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

## Writing tests
After you create a new lesson, you want to test your code to make sure it functions properly.
Inside `tests/stage/[stage name]/` folder, create a new test.py file, which must start with `test_`.
For example, the `s1_hello_python.py` lesson's corresponding test file is `test_s1_hello_python.py`.


Use the structure below to build your tests:
```python
from stage.[stage name].[lesson name] import route, data
from tests.utils import check_attributes, post


# This test function must declare on the top in order to test first.
# It checks the attribute is not missing inside the [lesson].py
# DO NOT REMOVE OR MOVE DOWN THIS FUNCTION !!!
def test_attributes():
    check_attributes(route, data)

# This is the main test function, everything you need just only req_data.
async def test_lesson(test_cli):
    req_data = {
        ...
        'your_filed_with_id': 'field_answer'
        ...
    }
    await post(cli=test_cli, url=route['url'], data=req_data)

# This function provide a inner function for further override.
# In case you want to customize any check.
# You can pick one to use.
# async def test_lesson(rest_cli):
#     
#     def override(res_data):
#         # Any other check you wan to do.
#
#     req_data = {
#         ...
#         'your_filed_with_id': 'field_answer'
#         ...
#     }
#     await post(cli=test_cli, url=route['url'], data=req_data, callback=override)
```

Of course, if you want to add more tests to make sure your lesson is healthy, go for it!
Remember to make sure every test for each lesson is in the same test file.
Please refer to test files in this project to see how to use `test_cli.post` requests to test your lessons!

For example:
```python
# I want a new test function named haruna_cute
async def test_haruna_cute(test_cli):
    ...
    req_data = {
        ...
        'desire_field_key': 'desire_data'
        ...
    }
    ...
```

## Testing Your Lessons
Once you made tests for your lesson, be sure to test it locally before making a pull request!
You can easily run all tests by executing `python -m pytest` on the command line. Or, if you only want to test your new functionality, run `python -m pytest tests/stage/[stage number]/[your_test_file_name.py]`

Pytest will alert you which of your tests fail so you can easily fix them! If you do not catch these locally, the repository has Travis integration to make sure your builds pass or fail, so be sure to check your pull request after you make it to see if you succeed!

Good luck!
