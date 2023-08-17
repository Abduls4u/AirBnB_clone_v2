#!/usr/bin/python3
'''do_deploy module'''
from fabric.api import run, put, env
import os
import 1-pack , 2-do_deploy_web_static.py
env.user = 'ubuntu'
env.hosts = ['100.26.122.31', '52.3.253.201']


def do_deploy(archive_path):
    ''' Creates and Distributes an archive to your web servers'''
    
