# Copyright (C) Simon Chopin <chopin.simon@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup

install_requires = [
    'fedmsg',
]

setup(
    name='fedmsg_meta_tanglu',
    version='0.1',
    description='fedmsg metadata providers for Tanglu deployment',
    long_description=
    '''This package provide metadata suited for the deployement of Fedmsg within the Tanglu infrastructure''',
    author='Matthias Klumpp',
    author_email='matthias@tenstral.net',
    license='Expat',
    install_requires=install_requires,
    packages=[
        'fedmsg_meta_tanglu',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'fedmsg.meta': [
            "debchanges=fedmsg_meta_debian.debmessenger:DebChangesProcessor",
            "debbugs=fedmsg_meta_debian.debmessenger:DebBugProcessor",
            "debexpo=fedmsg_meta_debian.debexpo:DebexpoProcessor",
        ]
    }
)