import os

from distutils.core import setup
from distutils.command.install import install as _install

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


class install(_install):
    """Specialized installer.

    The YUM plugins are not installed in the regular Python modules tree.
    """
    def initialize_options(self):
        _install.initialize_options(self)
        # Remove this line and self.root defaults to '.', which is not desired
        self.root = '/'

    def run(self):
        # Install the plugin code
        yumplugins_coderoot = os.path.join(self.root, "usr/lib/yum-plugins/")
        self.mkpath(yumplugins_coderoot, mode=0755)
        self.copy_file('nuke-newsave.py', yumplugins_coderoot)

        # Install the plugin conf
        yumplugins_confroot = os.path.join(self.root, "etc/yum/pluginconf.d/")
        self.mkpath(yumplugins_confroot, mode=0755)
        self.copy_file('nuke-newsave.conf', yumplugins_confroot)


setup(name='yum-plugin-nuke-newsave',
        version='2.0',
        description='Automatically remove the .rpmnew/.rpmsave files after a yum transaction',
        long_description=README,
        classifiers=[
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Topic :: System :: Installation/Setup",
            "Topic :: System :: Software Distribution",
            "Topic :: System :: Systems Administration",
            ],
        author='Mathieu Bridon',
        author_email='bochecha@fedoraproject.org',
        url='https://gitorious.org/yum-plugin-nuke-newsave/yum-plugin-nuke-newsave',
        license='GPLv3+',
        py_modules=['nuke-newsave'],
        requires = [
            # The following are not available as distutils modules, but listing
            # them here seems like the nice thing to do for package maintainers
            # "yum>=3.2.29", # Not tested with older releases (that means RHEL6)
            ],
        cmdclass={
            'install': install,
            },
        )
