from __future__ import annotations
from typing import List, Dict

from stage.lesson_setup import LessonSetup
from stage.lesson_answer import LessonAnswer
from utils import fields_generate

class Lesson:
    def __init__(
        self,
        index: str,  # should be int, wait for refactor
        setup: LessonSetup,
        title: str,
        author: str,
        description: List[str],
        code: List[str],
        answer: LessonAnswer,
    ):
        self.index = index
        self.setup = setup
        self.title = title
        self.author = author
        self.description = description
        self.code = code
        self.answer = answer
    
    def get_router_data(self) -> Dict:
        return {
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'code': self.code,
            'fields': fields_generate({'code': self.code}),
        }
    
    def verify_answer(self, stdout, stderr) -> bool:
        [expect_stdout, expect_stderr] = self.answer.get_expects()
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
    def deserialize(index: str, setup: LessonSetup, answer: LessonAnswer, data: List[str]) -> Lesson:
        return Lesson(
            index=index,
            setup=setup,
            answer=answer,
            title=data['title'],
            author=data['author'],
            description=data['description'],
            code=data['code'],
        )
