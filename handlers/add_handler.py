from __future__ import annotations
from typing import TYPE_CHECKING
import argparse
from datetime import datetime

if TYPE_CHECKING:
    from database import Db

command_name = "add"

def main(args: argparse.Namespace, db:Db) -> None:
    new_id = str(db.last_id + 1)
    db[new_id] = {
            "category_name": args.category_name,
            "cost": args.cost,
            "description": args.description,
            "CreatedAt": datetime.now().ctime(),
            "UpdatedAt": "",
    }

    db.save()


def apply_subparser(subparsers: argparse._SubParsersAction):
    add_subparser = subparsers.add_parser(
            "add",
            help="add expense to the database"
            )

    add_subparser.add_argument("category_name", type=str, help="category of the expense")
    add_subparser.add_argument("cost", type=float, help="how much money was spent")
    add_subparser.add_argument("description",
                               type=str,
                               nargs="?",
                               default="",
                               help="Optional. Description of expense"
                               )
    
