from collections import UserDict
from pathlib import Path
import json
import sys


class Db(UserDict):
    def __init__(self, *args, path: Path, last_index: int = 0, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path

        if self.data:
            try:
                self.last_index = int(next(reversed(self.data.keys())))
            except ValueError as err:
                self.corruption_handler(err)
        else:
            self.last_index = last_index


    def save(self) -> None:
        try:
            with self.path.open("w") as file:
                json.dump(self.data, file, indent=2)
        except FileNotFoundError:
            print(f"Database file which was open for this process was not\
                    found. Exiting...")
            sys.exit()

    def delete(self) -> None:
        self.path.unlink(missing_ok=True)

    def corruption_handler(self, error):
        i = input(f"Corrupted database file. Manually fix the issue\
        or delete database file.\n{error}\n\n\
                Do you want to delete database file? y/n:")
        if i == "y":
            self.delete()
            print("Database file deleted. Try running the programm again.")
        elif i == "n":
            print("Exiting without deleting the file...")
            sys.exit()



def load_db(path: Path) -> Db:
    try:
        with path.open() as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    db = Db(data, path=path)
    return db
