# Copyright (C) 2013 Simon Chopin <chopin.simon@gmail.com>
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

from __future__ import unicode_literals

from fedmsg.meta.base import BaseProcessor
import re

class DebexpoProcessor(BaseProcessor):
    __name__ = "pkgreview"
    __description__ = "What happens when one doesn't have upload rights just yet"
    __link__ = "http://pkgreview.tanglu.org"
    __docs__ = "Would be nice."
    __obj__ = "Mentoring"

    event2title = {
        'upload': "Package upload (mentors)",
        'remove': "Package removal (mentors)",
        'comment': "Comment on a package (mentors)",
    }

    def title(self, msg, **config):
        event = msg['topic'].split('.')[-1]
        return self.event2title.get(event, event)

    def subtitle(self, msg, **config):
        event = msg['topic'].split('.')[-1]
        content = msg['msg']
        if event == 'upload':
            return '{name} uploaded {source}_{version} on mentors'.format(
                    name=content['uploader'],
                    source=content['source'],
                    version=content['version']
            )
        if event == 'comment':
            return '{name} commented on {package} on mentors.'.format(
                    name=content['author_name'],
                    package=content['source']
        )
        if event == 'remove':
            return '{source}_{version} has been removed from mentors ({reason})'.format(**content)

        return ''

    def link(self, msg, **config):
        try:
            source = msg['msg']['source']
        except KeyError:
            return ''
        return 'http://pkgreview.tanglu.org/{}'.format(source)
