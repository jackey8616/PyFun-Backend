from __future__ import annotations
from typing import Dict

class LessonSetup:
    def __init__(
        self,
        file_path: str,
        type: str,
        url: str,
    ):
        self.file_path = file_path
        self.type = type
        self.url = url

    @staticmethod
    def deserialize(file_path: str, data: Dict[str]) -> LessonSetup:
        return LessonSetup(
            file_path=file_path,
            type=data['type'],
            url=data['url'],
        )
