from collections import UserDict
from pathlib import Path


class Db(UserDict):
    def __init__(self, *args, path: Path, last_index: int, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.last_index = last_index


    def save(self) -> None:
        pass


def load_db(path:str) -> Db:
    pass
