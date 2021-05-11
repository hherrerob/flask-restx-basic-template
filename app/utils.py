# -*- coding: iso-8859-1 -*-

import re
import hashlib
from unicodedata import normalize


def string_to_id(s):
    return int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**6


def standardize(keyword):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    keyword = normalize('NFKC', normalize('NFKD', keyword).translate(trans_tab))
    keyword = re.sub('[^A-Za-z0-9 ]+', '', keyword)
    return keyword.lower().strip()
