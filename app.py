from chalice import Chalice
import boto3
from datetime import datetime, timedelta

####
from pprint import pprint
####

app = Chalice(app_name='planecount')
client = boto3.client('cloudwatch')


@app.route('/')
def index():
    response = client.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'test',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'piaware',
                        'MetricName': 'frederick'
                    },
                    'Period': 60,
                    'Stat': 'Average',
                    'Unit': 'Count'
                }
            },
        ],
        StartTime=datetime.now() - timedelta(seconds=60),
        EndTime=datetime.now()
    )
    print(datetime.now())
    print(round(response.get('MetricDataResults')[0].get('Values')[0]))
    return {
        'plane_count': round(response.get('MetricDataResults')[0].get('Values')[0]),
        'date_time': str(datetime.now())
    }
