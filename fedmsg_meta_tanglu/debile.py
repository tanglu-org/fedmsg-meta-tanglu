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
import re

class DebileProcessor(BaseProcessor):
    __name__ = "debile"
    __description__ = "Our package building service"
    __link__ = "http://buildd.tanglu.org"
    __docs__ = "Would be nice."
    __obj__ = "Building"

    event2title = {
        'build': "Package build",
        'result': "Results",
        'comment': "Comment on a package (mentors)",
        'receive': "Results received",
    }

    def title(self, msg, **config):
        event = msg['topic'].split('.')[-1]
        return self.event2title.get(event, event)

    def subtitle(self, msg, **config):
        event = msg['topic'].split('.')[-1]
        content = msg['msg']
        state_str = "was successful"
        if content['failed']:
            state_str = "has failed"
        text = "Job '%s' for package '%s' in '%s' %s." % (content['job'], content['source'], content['suite'], state_str)

        return text

    def link(self, msg, **config):
        content = msg['msg']
        source = content['source']
        sourcepkg = ""
        version = ""
        if "(" in source:
            parts = source.split("(")
            sourcepkg = parts[0].strip()
            version = parts[1]
            if ")" in version:
                version = version.replace(")", "").strip()
        else:
            return ""

        url = "http://buildd.tanglu.org/job/%s/%s/%s/%s/" % (content['group'], sourcepkg, version, content['job_id'])
        return url
