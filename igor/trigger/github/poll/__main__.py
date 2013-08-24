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

import argparse
import json
import logging
import socket
import time
import urllib.request

import igor.order


def main():
    parser = argparse.ArgumentParser(
        prog=__package__,
        description='igor-ci github poll trigger')

    parser.add_argument(
        '--repo', required=True,
        help='name of repository, e.g. frasertweedale/elk')
    parser.add_argument(
        '--branch', default='master',
        help='name of branch to notify')
    parser.add_argument(
        '--interval', type=int, default=3600, metavar='N',
        help='polling interval in seconds')
    parser.add_argument(
        '--trigger', action='store_true',
        help='trigger immediately rather than wait for change')

    parser.add_argument(
        '--spec-uri', required=True, metavar='URI',
        help='location of igor-ci git repository')
    parser.add_argument(
        '--spec-ref', required=True, metavar='REF',
        help='name of the spec to build')

    parser.add_argument(
        '--host', required=True,
        help='hostname of igor-ci server')
    parser.add_argument(
        '--port', type=int, default=1602,
        help='port of igor-ci server')

    parser.add_argument('--logging', metavar='LEVEL')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    args = parser.parse_args()

    if args.logging:
        try:
            level = getattr(logging, args.logging.upper())
        except AttributeError:
            level = logging.INFO
        logging.basicConfig(level=level)

    poll_uri = 'https://api.github.com/repos/{}/git/refs/heads/{}'.format(
        args.repo, args.branch)
    source_uri = 'https://github.com/{}.git'.format(args.repo)

    count = 0
    prev_oid = None
    while True:
        try:
            data = urllib.request.urlopen(poll_uri).read().decode('UTF-8')
            oid = json.loads(data)['object']['sha']
            logging.debug('saw oid: {}'.format(oid))
            if prev_oid and oid != prev_oid or not prev_oid and args.trigger:
                desc = 'igor-trigger-github-poll {} {} {}'.format(
                    args.repo, args.branch, oid)
                logging.info('trigger: {}'.format(desc))
                order = igor.order.Order(
                    spec_uri=args.spec_uri,
                    spec_ref=args.spec_ref,
                    desc=desc,
                    source_uri=source_uri,
                )
                msgobj = {
                    'command': 'ordercreate',
                    'params': {'order': order.to_obj()}
                }
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.host, args.port))
                s.sendall(json.dumps(msgobj).encode('UTF-8') + b'\n')
                s.close()
                logging.debug('sent message')
            prev_oid = oid
        except:
            logging.exception('unhandled exception')
        logging.debug('going to sleep for {}s'.format(args.interval))
        time.sleep(args.interval)

main()
