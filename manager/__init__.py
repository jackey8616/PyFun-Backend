from __future__ import annotations
from typing import Dict
from os.path import isdir, join
from json import load

from stage import Stage
from stage.lesson import Lesson, LessonSetup, LessonAnswer
from utils import get_folder_files

class StageManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.stages = {}
    
    def get_stages(self) -> Dict[str, Stage]:
        return self.stages

    def build_from_static(self, static_folder = 'stage') -> StageManager:
        for (stage_name) in get_folder_files(static_folder):
            stage_file_path = join(static_folder, stage_name)
            if (isdir(stage_file_path) is False):
                continue
            if (stage_name not in self.stages):
                self.stages[stage_name] = {}

            lessons = {}
            for (lesson_file_name) in get_folder_files(stage_file_path):
                if (lesson_file_name.endswith('.json') is False):
                    continue
                
                index = lesson_file_name[1:lesson_file_name.index('_')]
                lesson_name = lesson_file_name.removeprefix('s{}_'.format(index)).removesuffix('.json')
                lesson_file_path = join(stage_file_path, lesson_file_name)
                with open(lesson_file_path, 'r') as lesson_file:
                    lesson_raw_data = load(lesson_file)
                    lesson = Lesson.deserialize(
                        index,
                        LessonSetup.deserialize(lesson_file_path, lesson_raw_data),
                        LessonAnswer.deserialize(lesson_raw_data),
                        lesson_raw_data,
                    )
                lessons[lesson_name] = lesson
            self.stages[stage_name] = Stage.deserialize(stage_name, lessons)
        return self
