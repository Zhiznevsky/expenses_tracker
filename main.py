import argparse

import database
import handlers

from collections.abc import Callable


commands: dict[str, Callable[[argparse.Namespace, database.Db], None]] = {}


def add_command(func: Callable) -> None:
    '''Decorator to add function to the commands global dict

    key = function's name until the first _
    value = function

    Example:
    @add_command
    def add_expense(...):
        ...

    Creates   "add": add_expense   entry in commands global dict'''

    first_word_from_name = func.__name__.split("_")[0]
    commands[first_word_from_name] = func

def initialize_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
            description="Track your expenses inside terminal. Use categories\
            for better understanding of your spending habits."
            )
    subparsers = parser.add_subparsers(dest="command" required=True)

    # for handler_name in (module for module in dir(handlers) if module.endswith("_handler")):
    

    return parser


def main():
    # Fill commands global dict with commands that represent the logic of the programm
    parser = initialize_parser()

    args = parser.parse_args()

    db = database.load_db(args.path)

    command = args.command
    commands[command](args, db)

    db.save()

 
if  __name__ == "__main__":
    main()
