from logging import Handler, getLogger, DEBUG
import os
from datetime import datetime
import time
"""
logging with multithreading
"""


class MPFileLogHandler(Handler):
    def __init__(self, file_path):
        self.__fd = os.open(file_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
        Handler.__init__(self)

    def emit(self, record):
        msg = "{}\n".format(self.format(record))
        os.write(self.__fd, msg.encode('utf-8'))


def process_log(p_off):
    logger_handler = MPFileLogHandler('/tmp/one_file_log.log')
    logger = getLogger('test')
    logger.addHandler(logger_handler)
    logger.setLevel(DEBUG)
    for x in range(0, 100):
        d = datetime.now()
        t_str = 'hello world' * 2000
        logger.info('{}:{}:p_off({}):pid({})'.format(t_str, d.strftime('%Y-%m-%d %H:%M:%S'), p_off, os.getpid()))


# process_log('/tmp/one_file_log.log')


with open('/tmp/one_file_log.log') as file:
    for line in file:
        print(len(line))
        time.sleep(1)
