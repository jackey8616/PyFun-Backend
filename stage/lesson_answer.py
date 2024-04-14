from __future__ import annotations
from typing import List, Dict

from utils import concat_code, data_execute

class LessonAnswer:
    def get_expects(self) -> List[str, str]:
        return [self.stdout, self.stderr]

    def verify_answer(self, stdout, stderr) -> bool:
        raise NotImplementedError

    @staticmethod
    def deserialize(data: Dict) -> LessonAnswer:
        expect = data['expect']
        if ('type' not in expect):
            return StdValidator.deserialize(data)

        match expect['type']:
            case 'std-validator':
                return StdValidator.deserialize(data)
            case 'runtime-validator':
                return RuntimeValidator.deserialize(data)
            case _:
                raise ValueError('Invalid type: %s' % data['type'])

class StdValidator(LessonAnswer):
    def __init__(self, stdout: List[str], stderr: List[str]):
        super().__init__()
        self.stdout = stdout
        self.stderr = stderr
    
    def verify_answer(self, stdout, stderr) -> bool:
        [expect_stdout, expect_stderr] = [self.stdout, self.stderr]
        if (len(expect_stdout) is not len(stdout) or len(expect_stderr) is not len(stderr)):
            return False

        for i in range(len(stdout)):
            if (stdout[i] != expect_stdout[i]):
                return False
        for i in range(len(stderr)):
            if (stderr[i] != expect_stderr[i]):
                return False
        
        return True

    @staticmethod
    def deserialize(data: Dict) -> LessonAnswer:
        expect = data['expect']
        return StdValidator(
            stdout=expect['stdout'] if 'stdout' in expect else [],
            stderr=expect['stderr'] if 'stderr' in expect else [],
        )

class RuntimeValidator(LessonAnswer):
    def __init__(self, source):
        super().__init__()
        self.source = source
    
    def verify_answer(self, stdout, stderr) -> bool:
        source = self.source
        source.append("print(validate(_____, _____))")

        code_data = concat_code({
            'code': source,
        }, {
            'field_1': stdout,
            'field_2': stderr,
        })
        validate_stdout, _ = data_execute(code_data)
        return validate_stdout[0] == 'True\n'

    @staticmethod
    def deserialize(data: Dict) -> LessonAnswer:
        expect = data['expect']
        return RuntimeValidator(source=expect['source'])
