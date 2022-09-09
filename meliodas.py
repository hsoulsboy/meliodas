import argparse
import sys

from meliodas.parsers.create import create_parser
from meliodas.parsers.list import list_parser
from meliodas.parsers.remove import remove_parser
from meliodas.parsers.remove_all import remove_all_parser

from meliodas.cron import *

def main():
    parser = argparse.ArgumentParser(prog="meliodas.py", description="Manage your cron jobs")
    sub_parsers = parser.add_subparsers()
    
    # 'Create' command sub-parser
    parser_create = create_parser.create(sub_parsers)
    parser_create.set_defaults(func=configureCronJob)
    
    # 'List' command sub-parser
    parser_list = list_parser.create(sub_parsers)
    parser_list.set_defaults(func=listCronJobs)

    # 'Remove' command sub-parser
    parser_remove = remove_parser.create(sub_parsers)
    parser_remove.set_defaults(func=removeCronJob)

    # 'Remove-All' command sub-parser
    parser_remove_all = remove_all_parser.create(sub_parsers)
    parser_remove_all.set_defaults(func=removeAllCronJobs)

    args = parser.parse_args()

    if len(sys.argv) > 1:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()