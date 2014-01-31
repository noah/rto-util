#
# slugify thanks to some random stackoverflow user

import re
from unicodedata import normalize
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

from os import stat
from pwd import getpwuid

def owner(path):
    return getpwuid(stat(path).st_uid).pw_name
