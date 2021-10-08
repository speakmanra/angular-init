# AGS Angular Init Script

### To get started

Clone this project to where you want your project to live.

Double click the init.sh file in finder, or run `sh init.sh` in terminal.

This script will create an Angular project with most of the dependencies we use across projects.

The script will always use the most recent version of Angular. To use a specific version, you can change `npm install -g @angular/cli@latest` to whatever version you would like to use in the init.sh file. Keep in mind you will most likely need to configure other dependency versions as well if you do this.

This project will need to be updated from time to time in order to maintain dependency compatibility.

### Structure

The init.sh file runs all of the commands required to initiate the project.

The resources folder contains pre written files that are copied to the project.

The scripts folder contains the python scripts that either copy or rewrite files.

### Changing dependencies

Eventually, packages will be upgraded and different versions must be used. For example, for Angular 12 you must use Typescript 4.3.5, when 4.4.3 is the most recent version. The console will usually tell you when errors like this happen. Make updates to the scripts whenever this happens.