import os
import sys

CRON_JOB = """# /etc/cron.d/meliodas: crontab entries for meliodas

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

{minute} {hour} {day_of_month} {month} {day_of_week} root {job_command}
"""

def configureCronJob(minute, hour, day_of_month, month, day_of_week, job_command):
    # Check if the user has root privileges
    if os.geteuid() != 0:
        print("The user doesn't have root privileges. Run the script with 'sudo'.")
        sys.exit(1)

    with open("/etc/cron.d/meliodas", "w") as f:
        f.writelines(CRON_JOB.format(
            minute=minute, 
            hour=hour, 
            day_of_month=day_of_month, 
            month=month, 
            day_of_week=day_of_week, 
            job_command=job_command
        )
    )