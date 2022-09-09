def create(sub_parsers):
    remove_parser = sub_parsers.add_parser("remove", help="Removes a cron job", description="Removes a cron job")
    remove_parser.add_argument("--id", type=int, required=True, help="Cron job ID")

    return remove_parser