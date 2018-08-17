""" Main ETL python """

### import statements

import os
import sys
import datetime
import argparse
import subprocess
import requests
import ConfigParser
import mylogger

### class/method definitions
def slack_notification(log, msg_json):
    """ Send messages to slack channel. Please ensure the SLACK_WEBHOOK system parameter is correct and accessible. """
    # Call ES service to remove history data first.
    slack_webhook = config.get(ARGS_P.env, 'SLACK_WEBHOOK')

    resp = requests.post(slack_webhook, data=msg_json, timeout=10)
    log.debug('URL: %s, Data: %s' % (slack_webhook, msg_json))
    if resp.status_code >= 400:
        log.error('status code %s, response %s' % (resp.status_code, resp.text))
    else:
        log.info('Slack msg sent: %s, %s, %s' % (UUID, resp.status_code, resp.text))

def exec_cmd(log, command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        log.debug('CMD resp: %s' % line[:-1])
    P.wait()
    if P.returncode != 0:
        raise Exception('Command return abnormal code status: %s' % P.returncode)

### Start runtime code ###
LOGGER = mylogger.NewLogger().get_logger()
RUN_DT = datetime.datetime.now()

config = ConfigParser.ConfigParser()
config.read('config.ini')
PARSER = argparse.ArgumentParser(description='A ETL script to dumping email data from MySQL, transforming the normalized data into a flat data schema and upload to Hive. This ETL refreshing logic will be fully updating.')
PARSER.add_argument('-e', action='store', dest='env', choices=['prod', 'dev'], default='prod', help='Environment flag parameter, prod or dev.')
ARGS_P = PARSER.parse_args()

LOGGER.info('============= Start =============')
LOGGER.info('joseph')
LOGGER.info(ARGS_P)
slack_webhook = config.get(ARGS_P.env, 'SLACK_WEBHOOK')
LOGGER.info(slack_webhook)

try:
    # TODO: Main logic here
    pass

    # LOGGER.info(config.get(ARGS_P.env, 'SLACK_WEBHOOK'))
    # slack_notification(LOGGER, "msg");
    # Load data from MYSQL to local tmp file

    # Upload data to hive.

except Exception, err:
    # log.error('ETL failed: %s' % err)
    msg = '{}'
    #slack_notification(LOGGER, msg)

LOGGER.info('============= END (%s) =============' % (datetime.datetime.now() - RUN_DT))
