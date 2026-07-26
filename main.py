import argparse
import importlib
from pkgutil import iter_modules

import database
import handlers

from collections.abc import Callable

DEFAULT_DB_PATH = "./db.json"

commands: dict[str, Callable[[argparse.Namespace, database.Db], None]] = {}


def initialize_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
            description="Track your expenses inside terminal. Use categories\
            for better understanding of your spending habits."
            )
    parser.add_argument("--db_path",
                        nargs=1,
                        default=DEFAULT_DB_PATH,
                        required=False,
                        dest="db_path",
                        help="Choose file to use as a database. Must be ,json",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for module_info in iter_modules(handlers.__path__):
        handler_module = importlib.import_module(f"handlers.{module_info.name}")

        commands[handler_module.command_name] = handler_module.main
        handler_module.apply_subparser(subparsers)

    return parser


def main():
    # Fill commands global dict with commands that represent the logic of the programm
    parser = initialize_parser()

    args = parser.parse_args()

    db = database.load_db(args.path)

    command = args.command
    commands[command](args, db)

 
if  __name__ == "__main__":
    main()
