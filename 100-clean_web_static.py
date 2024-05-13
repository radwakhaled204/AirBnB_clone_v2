#!/usr/bin/python3
# Script that deletes out-of-date archives, using the function do_clean

from fabric.api import env, run, local, lcd
from os.path import isdir

# Define the hosts and the user
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'

def do_clean(number=0):
    """Function that deletes out-of-date archives"""
    # Convert the number to an integer
    number = int(number)
    # If number is 0 or 1, keep only the most recent version of your archive
    if number == 0 or number == 1:
        number = 1
    else:
        # Otherwise, keep the number of versions specified
        number += 1
    # Delete all unnecessary archives in the versions folder
    with lcd("versions"):
        # Get the list of archive files sorted by date
        archives = local("ls -t", capture=True)
        # Split the list by newline
        archives = archives.split("\n")
        # Keep only the archives after the number to keep
        archives = archives[number:]
        # For each archive to delete
        for archive in archives:
            # Delete the file
            local("rm -f {}".format(archive))
    # Delete all unnecessary archives in the /data/web_static/releases folder of both of your web servers
    with cd("/data/web_static/releases"):
        # Get the list of archive folders sorted by date
        archives = run("ls -t")
        # Split the list by newline
        archives = archives.split("\n")
        # Keep only the archives after the number to keep
        archives = archives[number:]
        # For each archive to delete
        for archive in archives:
            # Delete the folder
            run("rm -rf {}".format(archive))
