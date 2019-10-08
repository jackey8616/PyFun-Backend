from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/one/if',
    'methods': ['GET', 'POST']
}



data = {
    'title': 'Tuples in Python',
    'description': [
        'Hello there!',
        'I see that you are a new face!',
        'Try to do some tuple problems in python'
    ],
    'code': [
# concatenate 2 tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
print(_____ + _____)

 
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

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = "(0,1,2,3,python,geek)\n"
            if stdout[0].decode() != ans:
                return False
            return True
    except Exception:
        return False

