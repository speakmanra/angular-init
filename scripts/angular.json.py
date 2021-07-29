import sys, json;

project_name = sys.argv[1]
package_file_path = '../' + project_name + '/angular.json'

with open(package_file_path, 'r+') as f:
  data = json.load(f)
  lintFile = open('./resources/files/angular.json.lint.json')
  lintData = json.load(lintFile)
  del data['projects'][project_name]['architect']['test']
  data['projects'][project_name]['architect'].update(lintData)

  final = json.dumps(data, indent=2)

  f.seek(0)
  f.write(final)
  f.truncate()