#!/usr/bin/python3
'''do_deploy module'''
from fabric.api import run, put, env
import os


def do_deploy(archive_path):
    '''Distributes an archive to your web servers'''

    try:
        if os.path.exists(archive_path):
            # get filename from the archive path
            filename_w_ext = os.path.basename(archive_path)
            # extract filename without extension
            filename_no_ext = os.path.splitext(os.path.basename(archive_path))[0]
            put(archive_path, '/tmp/')
            run('mkdir -p /data/web_static/releases/{}'.format(filename_no_ext))
            run('tar -xzf {} -C /data/web_static/releases/{}/'.format(
                '/tmp/' + filename_w_ext,
                filename_no_ext))
            run('rm /tmp/{}'.format(filename_w_ext))
            run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(filename_no_ext, filename_no_ext))
            run('rm -rf /data/web_static/releases/{}/web_static'
                .format(filename_no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
                .format(filename_no_ext))
            return (True)
    except Exception:
        return (False)
