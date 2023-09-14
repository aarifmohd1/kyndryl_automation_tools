from elasticsearch import Elasticsearch
import json

auth_data = '{"basic_auth": ["task_load_automation_lab", "{{ elastic_password }}"]}'
basic_auth = json.loads(auth_data)
json_document = '{{ results_machine_readable | regex_replace("\'", "\"") }}'
# json_document = {{ hello_world_json | to_json }}
es = Elasticsearch(
   [
      {
         'host': 'dp-elastic-eu1-prod-int.kyndryl.net',
#         'host': '158.87.50.131',
         'port': 443,
         'scheme': "https",
#          'use_ssl': True
      }
   ],
   **basic_auth,
   verify_certs=False,
   ssl_show_warn=False,
   request_timeout=30,
   max_retries=2,
   retry_on_timeout=True)
del basic_auth

# check ES status
es.cluster.health(wait_for_status='yellow')
assert es.cluster.health()['status'] in ('yellow', 'green')
print('Elastic connected.')

# push test data to ES
# resp=es.index(index='delivery.automation.lab.test', document='{ "hello": "world" }')
resp=es.index(index='{{ elastic_index }}', id='{{ date_since }}', document=json_document)
print(f"{resp} document loaded into Elasticsearch.")
# print(f"{len(resp[1])} document loading failed")
print(resp)
