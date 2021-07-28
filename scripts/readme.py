import os, sys

project_name = sys.argv[1]
package_file_path = '../' + project_name + '/README.md'

content = '''
# {}

## Website info

<Add website description here>

## Development server

This project was developed with and requires Node 12.

This project uses yarn. 

Run `yarn start` for a dev server. Navigate to `http://localhost:3000/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `yarn build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `yarn test` to execute the unit tests via Jest.

This project runs pre-commit tests and linters.

## Running end-to-end tests

Run `yarn e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

'''.format(project_name)

with open(package_file_path, 'r+') as f:
  f.seek(0)
  f.write(content)
  f.write('\n')
  f.truncate()
