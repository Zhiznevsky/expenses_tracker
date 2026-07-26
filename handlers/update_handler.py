from __future__ import annotations
from typing import TYPE_CHECKING
import argparse
from datetime import datetime

if TYPE_CHECKING:
    from database import Db

command_name = "update"

def main(args: argparse.Namespace, db:Db) -> None:
    entry = db[args.id]
    updated = False

    if args.category_name:
        entry["category_name"] = args.category_name
    if args.cost:
        entry["cost"] = args.cost
    if args.description:
        entry["description"] = args.description

    if updated:
        entry["UpdatedAt"] = datetime.now().ctime()

    db.save()


def apply_subparser(subparsers: argparse._SubParsersAction):
    add_subparser = subparsers.add_parser(
            "update",
            help="Update entry information"
            )

    add_subparser.add_argument("category_name",
                               type=str,
                               help="Optional. Category of the expense",
                               default="",
                               nargs="?")
    add_subparser.add_argument("cost",
                               type=float,
                               help="Optional. How much money was spent"
                               default="",
                               nargs="?")
    add_subparser.add_argument("description",
                               type=str,
                               nargs="?",
                               default="",
                               help="Optional. Description of expense"
                               )
    
