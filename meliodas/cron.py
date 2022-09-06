import os
import sys

DEFAULT_CRON_JOB = """# /etc/cron.d/meliodas: crontab entries for meliodas

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

{minute} {hour} {day_of_month} {month} {day_of_week} root {job_command}
"""

CRON_JOB = "{minute} {hour} {day_of_month} {month} {day_of_week} root {job_command}"

def configureCronJob(args):
    # Check if the user has root privileges
    if os.geteuid() != 0:
        print("The user doesn't have root privileges. Run the program with 'sudo'.")
        sys.exit(1)

    if not os.path.exists("/etc/cron.d/meliodas"):
        with open("/etc/cron.d/meliodas", "w") as f:
            f.writelines(DEFAULT_CRON_JOB.format(
                minute=args.minute,
                hour=args.hour,
                day_of_month=args.day_of_month,
                month=args.month,
                day_of_week=args.day_of_week,
                job_command=args.job_command
            )
        )
    else:
        with open("/etc/cron.d/meliodas", "a") as f:
            f.writelines(CRON_JOB.format(
                minute=args.minute,
                hour=args.hour,
                day_of_month=args.day_of_month,
                month=args.month,
                day_of_week=args.day_of_week,
                job_command=args.job_command
            )
        )

def listCronJobs(args):
    if not os.path.exists("/etc/cron.d/meliodas"):
        print("No cron jobs are set.")
        sys.exit(0)

    with open("/etc/cron.d/meliodas") as f:
        for i, line in enumerate(f):
            if "root" in line:
                print(f"Cron Job[{i}] = {line}")