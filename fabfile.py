from fabric.api import *
import os
import shutil
import sys

#from pelican.server import ComplexHTTPRequestHandler, socketserver


# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Github Pages configuration
env.github_pages_branch = "gh-pages"

SERVER = '127.0.0.1'
PORT = 8000


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)


def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')


def rebuild():
    """`clean` then `build`"""
    clean()
    build()


def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    socketserver.TCPServer.allow_reuse_address = True

    try:
        httpd = socketserver.TCPServer((SERVER, PORT), ComplexHTTPRequestHandler)
    except OSError as e:
        print("Could not listen on port %s, server %s." % (PORT, SERVER))
        sys.exit(getattr(e, 'exitcode', 1))

    print("Serving at https://%s:%s." % (SERVER, PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt as e:
        print("Shutting down server.")
        httpd.socket.close()


def publish():
    """Publish to GitHub Pages"""
    clean()
    local('pelican -s publishconf.py')
    local('echo blog.alexandrevicenzi.com > {deploy_path}/CNAME'.format(**env))
    local("echo $'User-agent: *\nSitemap: http://blog.alexandrevicenzi.com/sitemap.xml' > {deploy_path}/robots.txt".format(**env))
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))
