#!/usr/bin/python3
'''do_deploy module'''
from fabric.api import run, put, env
import os
from 1-pack_web_static.py import do_pack
from 2-do_deploy_web_static.py import do_deploy
env.user = 'ubuntu'
env.hosts = ['100.26.122.31', '52.3.253.201']


def do_deploy():
    ''' Creates and Distributes an archive to your web servers'''
    try:
        archive_path = do_pack()
        deploy = do_deploy(archive_path)
        return (deploy)
    except Exception:
        return (False)
