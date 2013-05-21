#-*- coding: utf-8 -*-
u"""
Fabric script to deploy
"""
# Fabric imports
from fabric.api import run, local, env, execute, put, sudo, cd
from fabric.api import hosts, task, with_settings, parallel
from fabric.utils import abort


DEPLOY_USER_CMD = "adduser {}"
CREATE_VENV_CMD = "virtualenv -p python2.7 venvs/pycourse"
ENABLE_VENV_CMD = "source venvs/pycourse/bin/activate"
INSTALL_READLINE_CMD = "easy_install readline"
INSTALL_REQS_CMD = "pip install -r {}"
PYDEMO_CLONE_CMD = "git clone https://github.com/pablito56/pydemo.git"
PYDEMO_INSTALL_CMD = "python setup.py install"

PYDEMO_FOLDER = "pydemo"
REQS_FILE = "requirements.txt"


if env.hosts == []:
    if env.user == 'pev' and not getattr(env, 'password', None):
        env.user = 'sysadmin'
        env.password = 'sysadmin'
    env.hosts = ['dev-enabl-py-01']


@task
def create_user(uername):
    """Create a new OS user
    """
    output = sudo(DEPLOY_USER_CMD.format(uername))


@task
def create_virtualenv():
    """Create user pycourse virtualenv
    """
    output = run(CREATE_VENV_CMD)


@task
def put_requirements():
    """Put requirements file
    """
    output = put(REQS_FILE)


@task
@parallel(pool_size=5)
def install_reqs():
    """Enable virtualenv and install requirements
    """
    output = run(ENABLE_VENV_CMD + "; " + INSTALL_REQS_CMD.format(REQS_FILE))


@task
def install_readline(uername):
    """Create a new OS user
    """
    run(ENABLE_VENV_CMD)
    output = run(INSTALL_READLINE_CMD)


@task
@hosts('localhost')
def create_users(prefix="team", number=15):
    """"Deploy needed OS users
    """
    for num in xrange(number):
        execute(create_user, prefix + "_" + str(num))


@task
@hosts('localhost')
@parallel(pool_size=5)
def install_users_reqs(prefix="team", number=15, skip=None):
    """"Enable users virtualenv and install requirements.txt
    """
    old_user = env.user
    old_password = env.password
    for num in xrange(number):
        if skip is not None:
            if num < int(skip):
                continue
        env.user = prefix + "_" + str(num)
        env.password = prefix + "_" + str(num)
        print "Excuting 'install_reqs' for user '{}'".format(env.user)
        execute(install_reqs)
    env.user = old_user
    env.password = old_password


@task
def install_pydemo():
    """Install pydemo
    """
    run("rm -rf pydemo")
    run(PYDEMO_CLONE_CMD)
    with cd(PYDEMO_FOLDER):
        output = run("../" + ENABLE_VENV_CMD + "; " + PYDEMO_INSTALL_CMD)


@task
@hosts('localhost')
@parallel(pool_size=5)
def install_users_pydemo(prefix="team", number=15, skip=None):
    """"Enable users virtualenv and install requirements.txt
    """
    old_user = env.user
    old_password = env.password
    for num in xrange(number):
        if skip is not None:
            if num < int(skip):
                continue
        env.user = prefix + "_" + str(num)
        env.password = prefix + "_" + str(num)
        print "Excuting 'install_pydemo' for user '{}'".format(env.user)
        execute(install_pydemo)
    env.user = old_user
    env.password = old_password


@task
@hosts('localhost')
def put_users_reqs(prefix="team", number=15):
    """"Deploy requirements.txt to each user
    """
    old_user = env.user
    old_password = env.password
    for num in xrange(number):
        env.user = prefix + "_" + str(num)
        env.password = prefix + "_" + str(num)
        execute(put_requirements)
    env.user = old_user
    env.password = old_password


@task
@hosts('localhost')
def create_users_venv(prefix="team", number=15):
    """"Create users virtualenvs
    """
    old_user = env.user
    old_password = env.password
    for num in xrange(number):
        env.user = prefix + "_" + str(num)
        env.password = prefix + "_" + str(num)
        execute(create_virtualenv)
    env.user = old_user
    env.password = old_password
