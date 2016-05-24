"""
 Serverless Module: Lambda Handler
 - Your lambda functions should be a thin wrapper around your own separate
   modules, to keep your code testable, reusable and AWS independent
"""

from __future__ import print_function

import json
import logging
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"))
import lib


log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    return lib.multi_show(event)
