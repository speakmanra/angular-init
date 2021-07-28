import os, sys
from shutil import copytree, copyfile

project_name = sys.argv[1]
package_file_path = '../' + project_name

copytree('./resources/store', package_file_path + '/src/app/store')
copytree('./resources/services', package_file_path + '/src/app/services')
copytree('./resources/notifications', package_file_path + '/src/app/notifications')
copytree('./resources/containers', package_file_path + '/src/app/containers')
copytree('./resources/components', package_file_path + '/src/app/components')
copytree('./resources/fonts', package_file_path + '/src/assets/fonts')
copyfile('./resources/files/app.component.html', package_file_path + '/src/app/app.component.html')

