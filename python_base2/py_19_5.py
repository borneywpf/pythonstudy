#!/usr/bin/env python

"""code list 19-3"""

import logging

logging.basicConfig(level = logging.INFO, filename = "mylog.log")

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

logging.debug('loging debug')

print 1 / 0

logging.info('The division succeeded')

logging.info('Ending program')