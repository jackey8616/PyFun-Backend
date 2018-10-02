
import traceback
from sanic.response import json

from utils import list_paths
from stage.one import pys as one_pys, add_route as one_add_route


async def index(request):
    stages = {
        'one': list_paths(one_pys)
    }
    return json({ 'success': True, 'data': stages })

def add_route(app):
    app.add_route(index, '/stage/', methods=['GET'])
    one_add_route(app)
