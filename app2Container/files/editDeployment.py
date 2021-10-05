import json
import sys

if(len(sys.argv) < 2):
    print("usage: editDeployment.py target")
    sys.exit(1)

target      = sys.argv[1]
try:
  with open('deployment.json') as f:
    data = json.load(f)
  f.close()
except:
  sys.exit(1)

if target == "ECS":
    data['ecsParameters']['createEcsArtifacts'] = True
    data['eksParameters']['createEksArtifacts'] = False
elif target == "EKS":
    data['eksParameters']['createEksArtifacts'] = True
    data['ecsParameters']['createEcsArtifacts'] = False
else:
    print("Unsupported target")
    sys.exit(1)

with open('deployment.json', 'w') as json_file:
  json.dump(data,json_file,ensure_ascii=True, indent=4,sort_keys=True)

json_file.close()
