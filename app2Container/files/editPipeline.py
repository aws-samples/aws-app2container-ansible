import json
import sys

if(len(sys.argv) < 5):
    print("usage: editPipeline.py target env clusterName serviceName")
    sys.exit(1)

target      = sys.argv[1]
env         = sys.argv[2]
clusterName = sys.argv[3]
if target == "ECS":
   serviceName = sys.argv[4]

try:
  with open('pipeline.json') as f:
    data = json.load(f)
  f.close()
except:
  sys.exit(1)

if target == "ECS":
  data['releaseInfo'][target][env]['enabled'] = True
  data['releaseInfo'][target][env]['clusterName'] = clusterName
  data['releaseInfo'][target][env]['serviceName'] = serviceName
elif target == "EKS":
  data['releaseInfo'][target][env]['enabled'] = True
  data['releaseInfo'][target][env]['clusterName'] = clusterName
else:
    print("Unsupported target")
    sys.exit(1)

with open('pipeline.json', 'w') as json_file:
  json.dump(data,json_file,ensure_ascii=True, indent=4,sort_keys=True)

json_file.close()
