# Copyright 2011 Network Box
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This work was inspired by the merge-conf plugin by Aurelien Bompard.
# You can find the sources for the merge-conf plugin in the yum-utils tree:
#     http://yum.baseurl.org/wiki


import os
from rpm import RPMFILE_CONFIG
from yum.plugins import TYPE_CORE

requires_api_version = '2.6'
plugin_type = (TYPE_CORE,)

always_nuke = False

def posttrans_hook(conduit):
    global always_nuke

    opts, args = conduit.getCmdLine()
    conf = conduit.getConf()

    if not always_nuke and not (opts and opts.nuke_newsave):
        return

    ts = conduit.getTsInfo()
    for tsmem in ts.getMembers():
        rpmdb = conduit.getRpmDB()
        packages = rpmdb.searchNevra(tsmem.po.name, tsmem.po.epoch, tsmem.po.version, tsmem.po.release, tsmem.po.arch)

        for package in packages:
            hdr = package.returnLocalHeader()
            files = hdr["filenames"]
            fileflags = hdr["fileflags"]
            filetuple = zip(files, fileflags)

            for file_name, flags in filetuple:
                if flags & RPMFILE_CONFIG:
                    new_conf = "%s.rpmnew" % file_name
                    if os.path.exists(new_conf):
                        os.unlink(new_conf)

                    save_conf = "%s.rpmsave" % file_name
                    if os.path.exists(save_conf):
                        os.unlink(save_conf)

def config_hook(conduit):
    global always_nuke
    always_nuke = conduit.confBool('main', 'always_nuke', default=False)
    parser = conduit.getOptParser()
    if parser:
        if hasattr(parser, 'plugin_option_group'):
            parser = parser.plugin_option_group

        parser.add_option('', '--nuke_newsave', dest='nuke_newsave',
                action='store_true', default=False,
                help="remove the .rpmnew/.rpmsave files after a yum transaction")
