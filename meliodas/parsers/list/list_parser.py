def create(sub_parsers):
    list_parser = sub_parsers.add_parser("list", help="Lists all cron jobs", description="Lists all cron jobs")
    list_parser.add_argument("--pretty", type=bool, const=True, nargs="?", help="Outputs the cron job in a prettier way")

    return list_parser