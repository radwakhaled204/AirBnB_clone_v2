#!/usr/bin/python3
# Script that generates a .tgz archive from contents of the web_static folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """Function that creates and returns the archive path"""
    # Create the folder versions if it doesn't exist
    local("mkdir -p versions")
    # Get the current datetime
    now = datetime.now()
    # Format the archive name with the datetime
    archive_path = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    # Compress the web_static folder to the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_path))
    # Return the archive path if successful, otherwise None
    if result.succeeded:
        return archive_path
    else:
        return None
