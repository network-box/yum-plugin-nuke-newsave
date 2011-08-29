About nuke-newsave
==================

Administrators of RPM-based systems are familiar with the .rpmnew and .rpmsave
files, those files that RPM creates to warn them that they should have a look
at the new configuration for the updated packages.

Usually, this is indeed a great information: the default configuration file for
the package has changed, and the local modifications might need to be checked.

But in some very specific cases, the admin might have valuable reasons to
ignore it. For example, when the local configuration is totally managed outside
of RPM.

In those cases, the .rpmnew and .rpmsave files just accumulate, take space
(generally very few, but in some deployments disk space might a valuable
resource), and are likely to cause confusion.

This is where the YUM nuke-newsave plugin enters.

.. warning:

    Please read the usage documentation before installing this plugin.


Install
=======

To use this YUM plugin, you need:

    - a RPM-managed operating system
    - YUM (TODO: specify minimum version)

Installing this plugin from the sources should be as simple as running one
command, as root::

    # python setup.py install

As for any Python module using Distutils, you can optionally specify the
installation root::

    # python setup.py install --root=/my/own/root

Hopefully, this plugin is already packaged in your favorite distribution, so
you can just run::

    # yum install yum-plugin-nuke-newsave


Usage
=====

.. warning::

    Installing this plugin will change the way YUM handles package updates in a
    way that could be dangerous if it is not the desired behavior. Install at
    your own risk.

The point of installing this plugin is to automate a repetitive and annoying
task: removing all those pesky .rpmnew/.rpmsave files. [#f1]_

This is why the plugin is enabled by default, to allow its usage with a minimum
of effort: install it, and forget about it.

However, it can be easily disabled, either by:

* removing the plugin, or
* setting `enabled=0' in `/etc/yum/pluginconf.d/nuke-newsave.conf'


Legal
=====

This project is distributed under the terms of the `GNU General Public License version 3 or later`_.

It was written as part of my work at `Network Box`_ as we needed it for our
own products.

We do not require you to assign your copyright or sign a legal document of any
kind before accepting your contributions to this project, so send us patches!

. _GNU General Public License version 3 or later: http://www.gnu.org/licenses/gpl.html

. _Network Box: http://www.network-box.com


.. rubric:: Footnotes

.. [#f1] The point is not that all .rpmnew and .rpmsave files are bad. They are
         indeed **generally a good thing**. In some very specific situations
	 though...
