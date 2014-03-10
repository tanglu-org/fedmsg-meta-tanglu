# Copyright (C) 2014 Matthias Klumpp <mak@debian.org>
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

class SynchrotronProcessor(BaseProcessor):
    __name__ = "synchrotron"
    __description__ = "Syncronizing Tanglu with Debian"
    __docs__ = "Would be nice."
    __link__ = "http://merges.tanglu.org"
    __obj__ = "Syncing"

    event2title = {
        'error': "Import error",
        'import': "Package import",
    }

    def title(self, msg, **config):
        event = msg['topic'].split('.')[-1]
        return self.event2title.get(event, event)

    def subtitle(self, msg, **config):
        event = msg['topic'].split('.')[-1]
        content = msg['msg']
        return content
