#!/usr/bin/env python3
'''Filtered logger'''
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,separator: str) -> List[str]:
    '''Filtering'''
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message
