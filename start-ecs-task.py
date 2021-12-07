import json
import boto3

client = boto3.client('ecs')

cluster = 'cluster-name'
task_name = 'task-definition-name' 
subnets = ['subnet-xxx']
security_groups = ['sg-xxx']

response = client.run_task(
        cluster=cluster,
        taskDefinition=task_name,
        count=1,
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': subnets,
                'securityGroups': security_groups,
                'assignPublicIp': 'ENABLED'
            }
        }
)
