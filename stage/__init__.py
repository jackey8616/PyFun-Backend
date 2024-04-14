from __future__ import annotations
from typing import Dict

from .lesson import Lesson

class Stage:
    def __init__(self, name: str, lessons: Dict[str, Lesson]):
        self.name = name
        self.lessons = lessons

    def get_lessons(self) -> Dict[str, Lesson]:
        return self.lessons

    @staticmethod
    def deserialize(name: str, lessons: Dict[str, Lesson]) -> Stage:
        return Stage(name, lessons)
