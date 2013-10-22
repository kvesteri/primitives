"""
primitives
----------

Data types you've always missed in Python
"""

from setuptools import setup, Command
import subprocess
import sys


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


PY3 = sys.version_info[0] == 3


extras_require = {
    'test': [
        'pytest>=2.2.3',
    ],
}


setup(
    name='primitives',
    version='0.1.0',
    url='https://github.com/kvesteri/primitives',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description="Data types you've always missed in Python",
    long_description=__doc__,
    packages=['primitives'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'validators>=0.2.0',
    ],
    extras_require=extras_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
