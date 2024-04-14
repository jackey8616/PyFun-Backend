
# Contributing new stage or lesson(V2)

Inside `stage` module.
There are currently two sub-modules named `one` and `two`.
Each sub-module folder should contain an `__init__.py` for auto import.

## Creating a new stage
Same as [V1](./CONTRIBUTING.md#creating-a-new-stage)

## Creating a new lesson

Inside the `stage/[stage_name]` folder (such as `stage/one`).  
Make sure there is a `__init__.py` file.  

Then, create a new file with an appropriate name to describe the lesson. Please see each each lessons's name
to get an idea of proper file naming convention. It is helpful if each file name describes the lesson's function name.  

**For Example:**
```
  You have a lesson you want to call hello_python, and you want it to be the 1st lesson in the stage,
  Then you should create a file called s1_hello_python.json like below:
```

Follow the code structure below to set up your lesson!
```json
{
    "type": "blank_form",              // Currently we only support blank form 
    "url": "/stage/one/hello_python",  // This is should be starts with /stage prefix, then [stage url], then [lesson url]
    "title": "Hello Python",          // Any title would show in Frontend.
    "author": "Official",             // Put your github or name here.
    "image": "",                      // image is optional, suggest use https
    "description": [
        "Hello there!",
        "I see that you are a new face!",
        "Try to say Hello to me!"
    ],
    // code with a array, each blank show with five underline(_),
    // frontend will automatically translate to <input> tag.
    // remember each line should escape with special character.
    "code": [
        "_____(\"_____\")"
    ],
    // Check below, there is two type of validator to use in expect field
    "expect": {
        "stdout": ["Hello Python\n"]
    }
}
```

### Answer validator
#### Std(out) Validator:
This validator strictly compares given stdout or stderr with code's output to determine correct or not.
```json
{
    ...
    "expect": {
        "type": "std-validator",  // If you omit this field, system will automatically process expect field as StdValidator
        "stdout": [
            "A\n",
            "B\n"
        ],
        "stderr": [] // Optional, for validate negative case
    }
    ...
}
```
** If you need further example, you can check /stage/one/s1_hello_python.json **

#### Runtime Validator:
This validator need you provides another source code, if your lessons each time generates different dynamic results, you can write some logics to verify it.

```json
{
    ...
    "expect": {
        "type": "runtime-validator", // Cannot omit this type specify.
        "source": [
            "def validate(input_stdout, input_stderr):",
            "    if input_stderr != []:",
            "        return False",
            "    ",
            "    # Other logics here",
            "    return True"
        ],
    },
    ...
}
```

The verify source code would look like this:
```python
def validate(input_stdout, input_stderr):
    if input_stderr != []:
        return False
    # Other logics here
    return True
```
You have to write in this format and must return a bool.
`input_stdout` is the stdout that the eval stdout of answer provides from frontend, and same as `input_stderr`.

** If you need further example, you can check /stage/one/s4_for_loop.json **

## Writing tests
After you create a new lesson, you want to test your code to make sure it functions properly.
Inside `tests/stage/[stage name]/` folder, create a new test.py file, which must start with `test_`.
For example, the `s1_hello_python.py` lesson's corresponding test file is `test_s1_hello_python.py`.


Use the structure below to build your tests:
```python
import pytest
from tests.utils import get, post


# This is the main test function, everything you need just only req_data.
@pytest.mark.asyncio
async def test_lesson(stage_manager, test_cli):
    lesson = stage_manager.get_stages()['stage_name'].get_lessons()['lesson_name']
    url = lesson.setup.url

    await get(cli=test_cli, url=url)
    req_data = {
        ...
        'your_filed_with_id': 'field_answer'
        ...
    }
    await post(cli=test_cli, url=url, data=req_data)
```

## Testing Your Lessons
Once you made tests for your lesson, be sure to test it locally before making a pull request!
You can easily run all tests by executing `python -m pytest` on the command line. Or, if you only want to test your new functionality, run `python -m pytest tests/stage/[stage name]/[your_test_file_name.py]`

Pytest will alert you which of your tests fail so you can easily fix them! If you do not catch these locally, the repository has Travis integration to make sure your builds pass or fail, so be sure to check your pull request after you make it to see if you succeed!

Good luck!
