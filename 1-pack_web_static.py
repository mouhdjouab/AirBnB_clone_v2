#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    "makr web_static folder to archive tgz"
    timest = datetime.now().strftime("%Y%m%d%H%M%S")
    arch_name = "web_static_{}.tgz".format(timest)

    if os.path.exists("versions") is False:
        local(" mkdir -p version ")

    result = local("tar -czvf versions/{} web_static".format(arch_name))

    # Check if the compression
    if result.succeeded:
        path = "versions/{}".format(arch_name)
        return path
    else:
        return None
