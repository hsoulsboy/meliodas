import argparse
from meliodas.parsers.create import create_parser
from meliodas.parsers.list import list_parser

from meliodas.cron import configureCronJob, listCronJobs

def main():
    parser = argparse.ArgumentParser(prog="meliodas.py", description="Manage your cron jobs")
    sub_parsers = parser.add_subparsers()
    
    # 'Create' command sub-parser
    parser_create = create_parser.create(sub_parsers)
    parser_create.set_defaults(func=configureCronJob)
    
    # 'List' command sub-parser
    parser_list = list_parser.create(sub_parsers)
    parser_list.set_defaults(func=listCronJobs)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()