#!/usr/bin/python3
"""
method that compress web_static folder of AirBnB Clone
"""
from fabric.api import local, run, env
from datetime import datetime
import os.path


def do_pack():
    """ Function Impelementation"""
    date = datetime.utcnow()
    tar_filename = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(date.year,
                                                                 date.month,
                                                                 date.day,
                                                                 date.hour,
                                                                 date.minute,
                                                                 date.second)

    if os.path.isdir("versions") is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local(f'tar -cvzf {tar_filename} web_static').failed is True:
        return None
    return tar_filename


if __name__ == "__main__":
    """Main Method"""
    do_pack()
