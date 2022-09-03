def create(sub_parsers):
    create_parser = sub_parsers.add_parser("create", help="Creates a cron job", description="Creates a cron job")
    create_parser.add_argument("--minute", type=str, required=True, help="Minute for cron job, e.g, 09")
    create_parser.add_argument("--hour", type=str, required=True, help="Hour for cron job, e.g, 14")
    create_parser.add_argument("--day-of-month", type=str, required=True, help="Day of month for cron job, e.g, 01")
    create_parser.add_argument("--month", type=str, required=True, help="Month for cron job, e.g, 02")
    create_parser.add_argument("--day-of-week", type=str, required=True, help="Day of week for cron job, e.g, 03")
    create_parser.add_argument("--job-command", type=str, required=True, help="job command, e.g, echo 'Hello'")

    return create_parser