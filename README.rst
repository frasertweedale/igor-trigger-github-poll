Synopsis
--------

::

  python -m igor.trigger.github.poll \
    --repo libgit2/libgit2 --branch development \
    --spec-uri ~/dev/igor-libgit2 --spec-ref build \
    --host localhost

  python -m igor.trigger.github.poll --help


Installation
------------

Dependencies:

- Python 3.3
- `igor-ci <https://github.com/frasertweedale/igor-ci>`_

Assuming ``python`` is ``python3.3``::

  git clone https://github.com/frasertweedale/igor-trigger-github-poll
  cd igor-trigger-github-poll
  python setup.py install


License
-------

::

  igor-ci is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.


Contributing
------------

The igor-trigger-github-poll source code is available from
https://github.com/frasertweedale/igor-trigger-github-poll.

Bug reports, patches, feature requests, code review and
documentation are welcomed.

To submit a patch, please use ``git send-email`` or generate a pull
request.  Write a `well formed commit message`_.  If your patch is
nontrivial, update the copyright notice at the top of each changed
file.

.. _well formed commit message: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
