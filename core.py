import json
from operator import itemgetter


#try:
file_json = open('source_file_2.json','r')
data_json = json.load(file_json)
data_json_sorted = sorted(data_json,key=itemgetter('priority'))

list_managers = []
list_projects = []
dict_managers = {}

for values in data_json_sorted:
    for i in values:
        for k in values['managers']:
            if(k not in dict_managers):
                dict_managers.update({k:[values[ 'name']]})
            else:
                dict_managers[k].append(values['name'])
        '''
        if(value['managers'] in dict_managers):
            dict_managers.update({value['managers']:value['name']})

        else:
            dict_managers['name'].append(value['name'])
'''
            

print(json.dumps(dict_managers, sort_keys=True, indent=4))
#except Exception as erro:
 #   print("ocorreu um erro ao carregar o arquivo")
  #  print("o erro é:{}".format(erro))