import os

from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(name='yum-plugin-nuke-newsave',
        version='0.1',
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
        )
