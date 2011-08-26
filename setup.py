import os

from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(name='yum-plugin-nuke-newsave',
        version='0.1',
        description='Automatically remove the .rpmnew/.rpmsave files after a yum transaction',
        long_description=README,
        classifiers=[
            "Programming Language :: Python",
            ],
        author='Mathieu Bridon',
        author_email='bochecha@fedoraproject.org',
        url='',
        license='GPLv3+',
        packages=[],
        requires = [
            # The following are not available as distutils modules
            # 'yum',
            ],
        )
