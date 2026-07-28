import argparse
import importlib
from pkgutil import iter_modules
from pathlib import Path

import database
import handlers

from collections.abc import Callable

DEFAULT_DB_PATH = Path("./db.json")

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

    # import handler modules
    for module_info in iter_modules(handlers.__path__):
        handler_module = importlib.import_module(f"handlers.{module_info.name}")

        commands[handler_module.command_name] = handler_module.main
        handler_module.apply_subparser(subparsers)

    return parser


def main():
    parser = initialize_parser()

    args = parser.parse_args()

    db = database.load_db(args.db_path)

    command = args.command
    commands[command](args, db)

 
if  __name__ == "__main__":
    main()
