# This file is part of igor-ci - the ghastly CI system
# Copyright (C) 2013  Fraser Tweedale
#
# igor-ci is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='igor-trigger-github-poll',
    version='0.1',
    author='Fraser Tweedale',
    author_email='frase@frase.id.au',
    url='https://github.com/frasertweedale/igor-trigger-github-poll',
    description='igor github poll trigger',
    long_description=readme,
    packages=['igor.trigger.github.poll'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Version Control',
    ]
)
