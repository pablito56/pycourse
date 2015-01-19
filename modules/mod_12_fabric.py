#-*- coding: utf-8 -*-
u"""
MOD: Fabric
"""


#===============================================================================
# - Fabric is a Python library and command-line tool for streamlining the use of
#    SSH for application deployment or systems administration tasks.
#
# - Fabric ralies on Paramiko, a library which implements SSH2 protocol.
#===============================================================================


from os import listdir
from fabric.api import run, local, env, prompt, execute, cd, settings
from fabric.api import parallel, task, serial, hosts


#===========================================================================
# EXERCISE:
# - For each function in this module, execute it with fabric script:
#    $ fab -f mod_12_fabric.py host_type -H team_0@dev-enabl-py-01,team_1@dev-enabl-py-01
#    $ fab -f mod_12_fabric.py host_and_date -H team_0@dev-enabl-py-01,team_1@dev-enabl-py-01
#    $ ...
#===========================================================================


@task
def host_type():
    '''Get host type'''
    run('uname -s')


@task
#@hosts('localhost')
def host_and_date():
    # Uncomment the decorator and execute again
    with cd('/tmp'):
        run('pwd')
        if prompt('Get date and host type? (y/n)').lower() == 'y':
            execute(host_type)
            execute(serial_date)


def not_a_task():
    '''This is not a task'''
    run('uname -a')


@task
def listdir_py():
    '''List current folder content'''
    print 'Listing folder...'
    listdir('.')


@task
def listdir_sh():
    '''List current folder content'''
    print 'Listing folder...'
    run('ls .')


@task
def date():
    '''Get current local date'''
    local('date')


@task
@hosts('localhost')
def local_date():
    '''Get current local date with decorator'''
    local('date')


@task
@serial
def serial_date():
    '''Get current date (serial)'''
    run('date')


@task
@parallel(pool_size=5)
def parallel_date():
    '''Get current date in parallel'''
    run('date')


@task
def fail():
    '''Task intended to fail'''
    run('cat fileWhichShouldNeverEverExist12345.txt')


@task
def warn_fail():
    '''Task intended to fail but just warn'''
    with(settings(warn_only=True)):
        run('cat fileWhichShouldNeverEverExist12345.txt')


@task
def listdir(folder='.'):
    '''List given folder content'''
    print 'Listing folder...'
    run('ls {0}'.format(folder))


#===============================================================================
# SOURCES:
#  - http://docs.fabfile.org/en/1.6/
#  - http://www.lag.net/paramiko/
#===============================================================================
