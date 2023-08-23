#!/usr/bin/python3
'''do_deploy module'''
from fabric.api import env, run, put
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.26.122.31', '52.3.253.201']
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


def do_deploy(archive_path):
    '''Distributes an archive to your web servers'''
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
    else:
        return (False)

def deploy():
    ''' Creates and Distributes an archive to your web servers'''
    archive_path = do_pack()
