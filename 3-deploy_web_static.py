#!/usr/bin/python3
# Script that creates and distributes an archive to your web servers, using the function deploy

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

# Define the hosts and the user
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'

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

def do_deploy(archive_path):
    """Function that distributes an archive to your web servers"""
    # Check if the archive file exists
    if not exists(archive_path):
        return False
    # Get the archive filename without the extension
    archive_file = archive_path.split('/')[-1]
    archive_name = archive_file.split('.')[0]
    # Upload the archive to the /tmp/ directory of the web server
    result = put(archive_path, '/tmp/{}'.format(archive_file))
    if not result.succeeded:
        return False
    # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    result = run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
    if not result.succeeded:
        return False
    result = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_file, archive_name))
    if not result.succeeded:
        return False
    # Delete the archive from the web server
    result = run('rm /tmp/{}'.format(archive_file))
    if not result.succeeded:
        return False
    # Move the web_static folder to the parent folder
    result = run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(archive_name, archive_name))
    if not result.succeeded:
        return False
    # Delete the web_static folder
    result = run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_name))
    if not result.succeeded:
        return False
    # Delete the symbolic link /data/web_static/current from the web server
    result = run('rm -rf /data/web_static/current')
    if not result.succeeded:
        return False
    # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code
    result = run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_name))
    if not result.succeeded:
        return False
    # Print a message indicating the new version is deployed
    print("New version deployed!")
    return True

def deploy():
    """Function that creates and distributes an archive to your web servers"""
    # Call the do_pack() function and store the path of the created archive
    archive_path = do_pack()
    # Return False if no archive has been created
    if archive_path is None:
        return False
    # Call the do_deploy(archive_path) function, using the new path of the new archive
    result = do_deploy(archive_path)
    # Return the return value of do_deploy
    return result
