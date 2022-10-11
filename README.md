# Meliodas

Command line interface dedicated to create, configure and manage cron jobs.

## Getting Started

First, clone the repo and access the created directory:
```
git clone https://github.com/hsoulsboy/meliodas
cd meliodas/
```

Then, execute the interface as follows:
```
$ python3 meliodas.py -h
usage: meliodas.py [-h] {create,list} ...

Manage your cron jobs

positional arguments:
  {create,list}
    create       Creates a cron job
    list         Lists all cron jobs

optional arguments:
  -h, --help     show this help message and exit
```

Each interface command has its own required and optional parameters. In order to understand how to use them, simply add the `-h` parameter at the end of the command:
```
$ python3 meliodas.py create -h
usage: meliodas.py create [-h] [--minute [MINUTE]] [--hour [HOUR]]
                          [--day-of-month [DAY_OF_MONTH]] [--month [MONTH]]
                          [--day-of-week [DAY_OF_WEEK]] --job-command
                          JOB_COMMAND

Creates a cron job

optional arguments:
  -h, --help            show this help message and exit
  --minute [MINUTE]     Minute for cron job, e.g, 09
  --hour [HOUR]         Hour for cron job, e.g, 14
  --day-of-month [DAY_OF_MONTH]
                        Day of month for cron job, e.g, 01
  --month [MONTH]       Month for cron job, e.g, 02
  --day-of-week [DAY_OF_WEEK]
                        Day of week for cron job, e.g, 03
  --job-command JOB_COMMAND
                        job command, e.g, echo 'Hello'
```

## Creating your first cron job

The `create` command should be used to create cron jobs. The following command exemplifies the creation of a job that will execute a script called `example_script.sh` under the `/tmp` directory at every 5 minutes:
```
$ python3 meliodas.py create --minute '*/5' --job-command /tmp/example_script.sh
```

The command above will add the following job to `/etc/cron.d/meliodas`:
```
*/5 * * * * root /tmp/example_script.sh
```
