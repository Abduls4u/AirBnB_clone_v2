#!/usr/bin/python3
'''do_deploy module'''
from fabric.api import run, put, env
import os


def do_deploy(archive_path):
    '''Distributes an archive to your web servers'''
    env.user = 'ubuntu'
    env.hosts = ['100.26.122.31', '52.3.253.201']
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        # get filename from the archive path
        filename_w_ext = os.path.basename(archive_path)
        # extract filename without extension
        filename_no_ext = os.path.splitext(archive_path)[0]
        run(f'mkdir -p /data/web_static/releases/{filename_no_ext}')
        run('tar -xzf {} -C /data/web_static/releases/{}/'.format(
            '/tmp/' + filename_w_ext,
            filename_no_ext))
        run('rm /tmp/{}'.format(filename_w_ext))
        run('mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/'.format(filename_no_ext, filename_no_ext))
        run(f'rm -rf /data/web_static/releases/{filename_no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{filename_no_ext}/ \
/data/web_static/current')
        return (True)
    else:
        return (False)
