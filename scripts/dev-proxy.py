import os, sys

project_name = sys.argv[1]
package_file_path = '../' + project_name + '/proxy.dev.config.json'

api = '''
{
  "/api": {
    "target": "<add-dev-env-here>",
    "changeOrigin": true,
    "pathRewrite": {
      "^/api": ""
    },
    "secure": true,
    "headers": {
      "Accept": "application/json",
      "Cache-Control": "no-cache"
    }
  }
}
  '''

with open(package_file_path, 'r+') as f:
  f.seek(0)
  f.write(api)
  f.write('\n')
  f.truncate()

