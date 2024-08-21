import sys
from datetime import datetime, timezone
import botocore
sys.path.append( '../')
from common.args import autoscaling_args
from common.boto_client_declaration import autoscaling_client
from common.logging_setup import logger

args, asg = autoscaling_args(), autoscaling_client(autoscaling_args())

def update_health_check_type(args):
    """
    Updates the health check type of the passed ASG.
    """

    start_time = datetime.now(timezone.utc)

    response = asg.update_auto_scaling_group(
        AutoScalingGroupName=args.asg_name,
        HealthCheckType=args.health_check_type
    )

    logger.info("")
    logger.info(f"HTTP Status Code: {response['ResponseMetadata']['HTTPStatusCode']}")
    logger.info(f"Request ID: {response['ResponseMetadata']['RequestId']}")
    logger.info(f"Retry Attempts: {response['ResponseMetadata']['RetryAttempts']}")

    total_time =  datetime.now(timezone.utc) - start_time



if __name__ == "__main__":
    logger.info("Autoscaling update functions.")
    update_health_check_type(args)