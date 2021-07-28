import os, sys

project_name = sys.argv[1]
package_file_path = '../' + project_name + '/.stylelintrc'

content = '''
{
  "rules": {
    "block-closing-brace-newline-before": "always-multi-line",
    "block-closing-brace-space-before": "always-single-line",
    "block-opening-brace-newline-after": "always-multi-line",
    "block-opening-brace-space-after": "always-single-line",
    "block-opening-brace-space-before": "always",
    "color-hex-case": "lower",
    "color-no-invalid-hex": true,
    "declaration-bang-space-before": "always",
    "declaration-block-semicolon-newline-after": "always",
    "declaration-block-trailing-semicolon": "always",
    "length-zero-no-unit": true,
    "selector-list-comma-newline-after": "always",
    "selector-list-comma-space-before": "never",
    "selector-pseudo-class-case": "lower",
    "selector-pseudo-element-case": "lower",
    "selector-type-case": "lower",
    "string-quotes": "double",
    "unit-case": "lower"
  }
}
'''

with open(package_file_path, 'r+') as f:
  f.seek(0)
  f.write(content)
  f.write('\n')
  f.truncate()
