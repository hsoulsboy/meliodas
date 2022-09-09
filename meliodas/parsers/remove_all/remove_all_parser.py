def create(sub_parsers):
    remove_all_parser = sub_parsers.add_parser("remove-all", help="Removes all cron jobs", description="Removes all cron jobs")

    return remove_all_parser