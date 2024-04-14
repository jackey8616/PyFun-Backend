from sanic.response import json

async def favicon(request):
    return json({})

async def index(request):
    return json({'success': True, 'data': 'Hello World!'})
