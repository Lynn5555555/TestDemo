import yaml
import os

root_path = os.path.dirname(os.path.dirname(__file__))

#print(yaml.load(open(root_path + "/data/caseData.yaml"), Loader=yaml.FullLoader))



info = [{"name": "lll", "age": "15", "sex": "女"}, {"name": "ggg", "age": "1", "sex": None}]

with open(root_path + '/data/text_file', 'w') as s:
    yaml.dump(info, stream=s)