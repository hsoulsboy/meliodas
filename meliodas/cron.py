import os
import sys

DEFAULT_CRON_JOB = """# /etc/cron.d/meliodas: crontab entries for meliodas

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

{minute} {hour} {day_of_month} {month} {day_of_week} root {job_command}
"""

CRON_JOB = "{minute} {hour} {day_of_month} {month} {day_of_week} root {job_command}\n"

def configureCronJob(args):
    # Run it with sudo if the user has no root privileges
    if os.geteuid() != 0:
        os.execvp('sudo', ['sudo', 'python3'] + sys.argv)

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
        counter = 1
        for line in f:
            if "root" in line:
                print(f"Cron Job ID: {counter}")
                
                print("Configured job:")
                if args.pretty:
                    minute, hour, day_of_month, month, day_of_week, user, job_command = parseCronJob(line)

                    print(f"Hour: {hour}")
                    print(f"Minute: {minute}")
                    print(f"Day of Week: {day_of_week}")
                    print(f"Day of Month: {day_of_month}")
                    print(f"Month: {month}")
                    print(f"User: {user}")

                    job = " ".join(job_command)
                    print(f"Job Command: {job}")

                    print("---------------------")
                else:
                    print(line)

                    print("---------------------")

                counter += 1

def parseCronJob(job):
    minute, hour, day_of_month, month, day_of_week, user = job.split(" ")[:6]
    job_command = job.split(" ")[6:]
    return minute, hour, day_of_month, month, day_of_week, user, job_command