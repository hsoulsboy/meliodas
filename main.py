import argparse
from cron import configureCronJob

def main():
    parser = argparse.ArgumentParser(prog="Meliodas", description="Manage your cron jobs", add_help=True)
    parser.add_argument("--minute", type=str, required=True, help="Minute for cron job, e.g, 09")
    parser.add_argument("--hour", type=str, required=True, help="Hour for cron job, e.g, 14")
    parser.add_argument("--day-of-month", type=str, required=True, help="Day of month for cron job, e.g, 01")
    parser.add_argument("--month", type=str, required=True, help="Month for cron job, e.g, 02")
    parser.add_argument("--day-of-week", type=str, required=True, help="Day of week for cron job, e.g, 03")
    parser.add_argument("--job-command", type=str, required=True, help="job command, e.g, echo 'Hello'")

    args = parser.parse_args()
    print(args)

    configureCronJob(args.minute, args.hour, args.day_of_month, args.month, args.day_of_week, args.job_command)

if __name__ == "__main__":
    main()