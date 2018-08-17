""" Personal logger Class """

### import statements

import sys
import os
import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler


### class/method definitions

class NewLogger:
    """ Personal logger Class """

    def __init__(self):
        """ Constructor """
        self.logger = logging.getLogger()


    def get_logger(self, level='INFO', logging_method=['stdout'], log_path='', log_format='%(asctime)s - %(process)d~%(thread)d %(levelname)s - %(message)s', file_rolling_period='D', interval=1, backup_count=7):
        """

        Return logger according input parameters
        Available types:
        - stdout: Standard system output.
        - timebased: Time based file rolling logger.
        - filebasic: Standard file based logger, no file rolling function.

        """

        if level == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        elif level == 'WARN':
            self.logger.setLevel(logging.WARN)
        elif level == 'ERROR':
            self.logger.setLevel(logging.ERROR)
        else:
            self.logger.setLevel(logging.INFO)

        if 'stdout' in logging_method:
            handler = logging.StreamHandler(sys.stdout)

        if 'timebased' in logging_method:
            p_dir = os.path.abspath(os.path.join(log_path, os.path.pardir))
            if not os.path.isdir(p_dir):
                os.makedirs(p_dir)

            handler = TimedRotatingFileHandler(log_path, when=file_rolling_period, interval=interval, backupCount=backup_count)

        elif 'filebasic' in logging_method:
            p_dir = os.path.abspath(os.path.join(log_path, os.path.pardir))
            if not os.path.isdir(p_dir):
                os.makedirs(p_dir)

            handler = logging.FileHandler(log_path)

        handler.setFormatter(logging.Formatter(log_format, '%m/%d/%Y_%H:%M:%S'))
        self.logger.addHandler(handler)

        return self.logger

# Testing only:
# lg = NewLogger().get_logger(log_path='./logs/mylogger.log', logging_method=['filebasic'])
# lg.info('HAHAHA')
# lg.error('HAHAHA')

# lg2 = NewLogger().get_logger()
# lg2.info('III')
# lg2.error('EEE')
