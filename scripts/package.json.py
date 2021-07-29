import os, sys

project_name = sys.argv[1]
package_file_path = '../' + project_name + '/package.json'

with open(package_file_path, 'r+') as f:
  lines = f.read().splitlines()
  lineArr = []
  for i, line in enumerate(lines):
    if i == 4:
      lineArr.append('    "ng": "ng",')
      lineArr.append('    "start": "ng serve --port 3000",')
      lineArr.append('    "build": "ng build",')
      lineArr.append('    "test": "jest --watch --detectOpenHandles",')
      lineArr.append('    "lint": "ng lint ' + project_name + ' --type-check",')
      lineArr.append('    "stylelint": "stylelint \\"src/**/*.scss\\"",')
      lineArr.append('    "prettier": "prettier --parser typescript --trailing-comma none --single-quote --write \\"./**/*.ts\\"",')
      lineArr.append('    "prettier:scss": "prettier --parser scss --write \\"./**/*.scss\\"",')
      lineArr.append('    "e2e": "ng e2e"')
      lineArr.append('  },')
      lineArr.append('  "jest": {')
      lineArr.append('    "preset": "jest-preset-angular",')
      lineArr.append('    "setupFilesAfterEnv": [')
      lineArr.append('      "<rootDir>/src/setup-jest.ts"')
      lineArr.append('    ],')
      lineArr.append('    "globals": {')
      lineArr.append('      "ts-jest": {')
      lineArr.append('        "tsConfig": "<rootDir>/tsconfig.spec.json",')
      lineArr.append('        "stringifyContentPathRegex": "\\\\.html$"')
      lineArr.append('      }')
      lineArr.append('    },')
      lineArr.append('    "testPathIgnorePatterns": [')
      lineArr.append('      "<rootDir>/node_modules/",')
      lineArr.append('      "<rootDir>/dist/"')
      lineArr.append('    ]')
      lineArr.append('  },')
      lineArr.append('  "husky": {')
      lineArr.append('    "hooks": {')
      lineArr.append('      "pre-commit": "yarn build && yarn prettier && yarn prettier:scss && yarn lint && yarn stylelint && jest && git add ."')
      lineArr.append('    }')
      lineArr.append('  },')
      continue
    if i > 4 and i < 10:
      continue
    else:
      lineArr.append(line)
  f.seek(0)
  f.write('\n'.join(lineArr))
  f.write('\n')
  f.truncate()
