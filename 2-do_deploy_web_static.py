#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path
from os.path import exists


env.hosts = ['54.167.181.61', '54.227.197.16']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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

    except Exception as e:
        return False
