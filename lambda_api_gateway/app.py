import json

import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(event)
    logger.info(context)

    now = datetime.datetime.now()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello api gateway. the time is {}".format(now),
        }),
    }
