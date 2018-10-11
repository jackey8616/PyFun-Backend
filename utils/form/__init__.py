import traceback
from sanic.response import json

from utils import concat_code, data_execute


def blank_form(data, request, answer):
    try:
        if request.method == 'GET':
            return json({'success': True, 'data': data})
        else:
            code_data = concat_code(data, request.json)
            stdout, stderr = data_execute(code_data)
            result = answer(stdout, stderr)
            return json({
                'success': True,
                'data': {
                    'result': result,
                    'stdout': stdout,
                    'stderr': stderr
                }
            })
    except Exception:
        return json({'fail': True, 'error': traceback.format_exc()})
