#!/usr/bin/python3
from fabric.api import *
from os.path import exists
from datetime import datetime
import os

env.hosts = ['54.167.181.61', '54.227.197.16']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_file = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_file))
        return archive_file
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_folder = "/data/web_static/releases/{}".format(
            archive_name.split(".")[0])

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(archive_folder))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, archive_folder))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo mv {}/web_static/* {}"
            .format(archive_folder, archive_folder))
        run("sudo rm -rf {}/web_static".format(archive_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(archive_folder))
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
