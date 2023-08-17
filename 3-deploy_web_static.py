#!/usr/bin/python3
'''do_deploy module'''
from fabric.api import env
import importlib
module_name1 = '1-pack_web_static'
module_name2 = '2-do_deploy_web_static'
module = importlib.import_module(module_name1)
module2 = importlib.import_module(module_name2)
do_pack = module.do_pack
do_deploy = module2.do_deploy
env.user = 'ubuntu'
env.hosts = ['100.26.122.31', '52.3.253.201']


def deploy():
    ''' Creates and Distributes an archive to your web servers'''
    try:
        archive_path = do_pack()
        deploy = do_deploy(archive_path)
        return (deploy)
    except Exception:
        return (False)
