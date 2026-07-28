from __future__ import annotations
from typing import TYPE_CHECKING
import argparse
from datetime import datetime
import sys


if TYPE_CHECKING:
    from database import Db

command_name = "update"

def main(args: argparse.Namespace, db:Db) -> None:
    entry = db[str(args.id)]
    updated = False

    if args.category_name:
        if args.category_name in db.category_names:
            entry["category_name"] = args.category_name
            updated = True
        else:
            print(f"No such category {args.category_name}")
            sys.exit()
    if args.cost:
        entry["cost"] = args.cost
        updated = True
    if args.description:
        updated = True
        entry["description"] = args.description

    if updated:
        entry["UpdatedAt"] = datetime.now().ctime()

    db.save()


def apply_subparser(subparsers: argparse._SubParsersAction):
    update_subparser = subparsers.add_parser(
            "update",
            help="Update entry information"
            )
    
    update_subparser.add_argument("id", type=int)
    update_subparser.add_argument("--category_name",
                               type=str,
                               help="Optional. Category of the expense",
                               default=None,
                               nargs="?")
    update_subparser.add_argument("--cost",
                               type=float,
                               help="Optional. How much money was spent",
                               default=None,
                               nargs="?")
    update_subparser.add_argument("--description",
                               type=str,
                               nargs="?",
                               default=None,
                               help="Optional. Description of expense"
                               )
    
