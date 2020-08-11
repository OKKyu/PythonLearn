#! python3
# -*- coding:utf-8 -*-

import traceback
import logging
logging.basicConfig(filename="./logging.log",level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

print(logging.DEBUG)
print(logging.CRITICAL)

try:
    logging.debug('debug message.')
    logging.info('info message.')
    logging.warn('warning message.')
    raise Exception('exception has occured!!')
    logging.warn('warning2 message.')
except Exception as ex:
    logging.error('error message.' + '\n' + traceback.format_exc())
    logging.fatal('fatal error message.' + '\n' + traceback.format_exc())
finally:
    pass
