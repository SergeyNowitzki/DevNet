# -*- coding: utf-8 -*-
import re
match = re.search('((\d+)\D(\d+))','The Adventures of Batwoman 345-123456')
print(match.groups())
