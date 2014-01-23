## About nuke-newsave

Administrators of RPM-based systems are familiar with the `.rpmnew` and
`.rpmsave` files, those files that RPM creates to warn them that they should
have a look at the new configuration for the updated packages.

Usually, this is indeed a great information: the default configuration file for
the package has changed, and the local modifications might need to be checked.

But in some very specific cases, the admin might have valuable reasons to
ignore it. For example, when the local configuration is totally managed outside
of RPM.

In those cases, the `.rpmnew` and `.rpmsave` files just accumulate, take space
(generally very few, but in some deployments disk space might be a valuable
resource), and are likely to cause confusion.

This is where the Yum nuke-newsave plugin enters.


## Warning

I can't stress this enough: **running this plugin will change the way Yum
handles package updates in a way that could be dangerous if it is not the
desired behavior**.

Use at your own risk.


## Install

To use this Yum plugin, you need:

* a RPM-managed operating system
* Yum (TODO: specify minimum version)

Installing this plugin from the sources should be as simple as running one
command, as root:

```
# python setup.py install
```

Hopefully, this plugin is already packaged in your favorite distribution, so
you can just run:

```
# yum install yum-plugin-nuke-newsave
```


## Usage

The plugin is enabled by default, but won't do anything unless it is told to.

There are two ways to let the plugin know you want it to act on the `*.rpmnew`
and `*.rpmsave` files:

* only for one transaction, passing the `--nuke_newsave` option to YUM
* permanently, by setting the `always_nuke` option to `1` in the
  `/etc/yum/pluginconf.d/nuke-newsave.conf` file.


## Legal

This project is distributed under the terms of the
[GNU General Public License version 3 or later](http://www.gnu.org/licenses/gpl.html).

It was written as part of my work at [Network Box](http://www.network-box.com)
as we needed it for our own products.

We do not require you to assign your copyright or sign a legal document of any
kind before accepting your contributions to this project, so send us patches!
