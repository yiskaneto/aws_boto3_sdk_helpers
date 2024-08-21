import sys
from datetime import datetime, timezone, timedelta
import botocore
sys.path.append( '../')
from common.args import elastic_beanstalk_args
from common.boto_client_declaration import elastic_beanstalk_client
from common.logging_setup import logger

args, eb = elastic_beanstalk_args(), elastic_beanstalk_client(elastic_beanstalk_args())

def eb_describe_environments(args):
    """
    Docstrings to be done
    """
    
    start_time = datetime.now(timezone.utc)

    print(f"Current time: {start_time}")
    ## How many hours to check in the past to monitor newly created EB environments
    max_hours_elastic_beanstalk_new_environments = 2
    past_new_elastic_beanstalk_env = start_time  - timedelta(
        hours=max_hours_elastic_beanstalk_new_environments
        )
    logger.info(f"Past time   : {past_new_elastic_beanstalk_env}\n")
    
    response = eb.describe_environments()

    for env in response['Environments']:
        if env['DateCreated'] > past_new_elastic_beanstalk_env:
            logger.info(f"{env['ApplicationName']} is a new environment")
            logger.info(f"Date Created: {env['DateCreated']}\n")
        elif env['DateCreated'] < past_new_elastic_beanstalk_env:
            logger.info(f"{env['ApplicationName']} was deployed over {max_hours_elastic_beanstalk_new_environments} hours ago, skipping")
            logger.info(f"Date Created: {env['DateCreated']}\n")
        # print(f"Application Name: {env['ApplicationName']}")
        # print(f"Environment Name: {env['EnvironmentName']}")
        # print(f"Date Created: {env['DateCreated']}")
        # print(f"Date Status: {env['Status']}\n")

    total_time =  datetime.now(timezone.utc) - start_time

if __name__ == "__main__":
    logger.info("Elastic Beanstalk describe functions.")
    # eb_describe_environments(args)