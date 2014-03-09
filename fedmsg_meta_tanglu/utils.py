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

import re

mail_regexp = re.compile('(?P<name>.*) <(?P<email>.*)>')
login_regexp = re.compile('(?P<login>.*)@debian\.org$')

def email2login(email):
    match = login_regexp.match(email)
    if match:
        return match.groupdict()['login']
    return None

def format_from(from_field):
    match = mail_regexp.match(from_field)
    if match:
        name, login = match.groupdict()['name'], email2login(match.groupdict()['email'])
        if login:
            return u'{name} ({login})'.format(name=name, login=login)
    return from_field

