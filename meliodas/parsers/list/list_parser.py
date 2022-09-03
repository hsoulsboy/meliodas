def create(sub_parsers):
    list_parser = sub_parsers.add_parser("list", help="Lists all cron jobs", description="Lists all cron jobs")

    return list_parser