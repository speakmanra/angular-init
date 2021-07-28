import os, sys
from shutil import copytree

project_name = sys.argv[1]
package_file_path = '../' + project_name

style_scss_content = '''
// Setup Custom Fonts
$font-path: "/assets/fonts";

// @font-face Setup
@import "./assets/fonts/usarmy/index";

// Get the config. This is needed in every component scss file.
@import "./styles/config";

// Material Icons
@import url("https://fonts.googleapis.com/icon?family=Material+Icons");

// Normalize
@import "~normalize-scss/sass/normalize/import-now";

// Get partials
@import "./styles/partials/all";

html,
body {
  height: 100%;
}

body {
  margin: 0;
}

'''

with open(package_file_path + '/src/styles.scss', 'r+') as f:
  f.seek(0)
  f.write(style_scss_content)
  f.write('\n')
  f.truncate()

copytree('./resources/styles', package_file_path + '/src/styles')
