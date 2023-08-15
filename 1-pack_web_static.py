#!/usr/bin/python3
'''do_pack module'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''generates a .tgz archive from the contents of the web_static'''
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = 'web_static_' + time + '.tgz'
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(archive))
        return ('versions/{}'.format(archive))
    except Exception:
        return (None)
