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


class DebileProcessor(BaseProcessor):
    __name__ = "debile"
    __description__ = "Our package building service"
    __link__ = "http://buildd.tanglu.org"
    __docs__ = "Would be nice."
    __obj__ = "Building"

    def title(self, msg, **config):
        mod = msg['topic'].split('.')[-2]
        event = msg['topic'].split('.')[-1]

        if event == "start" and mod == "job":
            return "Job assigned"

        if event == "complete" and mod == "job":
            return "Job completed"

        if event == "abort" and mod == "job":
            return "Job aborted"

        if event == "receive" and mod == "result":
            return "Job results received"

        elif event == "accept" and mod == "source":
            return "Source accepted"

        elif event == "accept" and mod == "binary":
            return "Binary accepted"

        return event

    def subtitle(self, msg, **config):
        mod = msg['topic'].split('.')[-2]
        event = msg['topic'].split('.')[-1]

        if event == "start" and mod == "job":
            job = msg['msg']
            return "Job '%s' for package '%s' in suite '%s' assigned to '%s'." % (job['name'], job['source'], job['suite'], job['builder']['name'])

        if event == "complete" and mod == "job":
            job = msg['msg']
            return "Job '%s' for package '%s' in suite '%s' completed by '%s'." % (job['name'], job['source'], job['suite'], job['builder']['name'])

        if event == "abort" and mod == "job":
            job = msg['msg']
            return "Job '%s' for package '%s' in suite '%s' aborted by '%s'." % (job['name'], job['source'], job['suite'], job['builder']['name'])

        if event == "receive" and mod == "result":
            result = msg['msg']
            job = result['job_obj']
            state_str = "has failed" if result['failed'] else "was successful"
            return "Job '%s' for package '%s' in suite '%s' %s." % (job['name'], job['source'], job['suite'], state_str)

        if event == "accept" and mod == "source":
            source = msg['msg']
            return "Source package '%s (%s)' in suite '%s' was accepted by the build system." % (source['name'], source['version'], source['suite'])

        if event == "accept" and mod == "binary":
            binary = msg['msg']
            return "Binary package '%s (%s)' for arch '%s' in suite '%s' was accepted by the build system." % (binary['name'], binary['version'], binary['arch'], binary['suite'])

        return msg['msg']

    def link(self, msg, **config):
        mod = msg['topic'].split('.')[-2]

        if mod == "job":
            job = msg['msg']
            source = msg['msg']['source_obj']

        if mod == "result" or mod == "binary":
            job = msg['msg']['job_obj']
            source = msg['msg']['source_obj']

        if mod == "source":
            job = None
            source = msg['msg']

        if job:
            return "http://buildd.tanglu.org/job/%s/%s/%s/%s/" % (source['group'], source['name'], source['version'], job['id'])

        if source:
            return "http://buildd.tanglu.org/source/%s/%s/%s/" % (source['group'], source['name'], source['version'])

        return None
