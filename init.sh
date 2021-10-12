#!/bin/sh

cd $(dirname $0)

# Get user to define the project name
read  -p "Project Name:" projectName

# Update Angular CLI
echo "Updating global Angular CLI to 12.1.4..."
npm install -g @angular/cli@12.1.4

echo  "Creating AGS project "$projectName"..."

# Step out of directory
cd ../

# Create Angular project
ng new $projectName --style scss --routing false

# If the command succeeded, there should be a folder with the name of $projectName. 
# If not, ng new has failed, and errors should show above in the ng new code block.
if [[ ! -d "./$projectName" ]] 
then
    echo "Something went wrong while initiating the project. Check above for errors."
    exit 1
fi


# cd into project
cd ./$projectName

# Install our default dependencies
# Some of these will need to be changed from time to time. As Angular releases new versions, certain versions of packages
# such as Typescript might need to be used. 
echo 'Installing additional dependencies...'
yarn add @angular/router @ngrx/store @ngrx/router @ngrx/effects @ngrx/router-store ngrx-store-localstorage normalize-scss rxjs@6.6.0 @angular/cdk ngrx-store-freeze @ngrx/store-devtools @angular/material
echo 'Installing additional dev dependencies...'
yarn add -D jest husky@4.2.5 jest-preset-angular typescript@4.3.5 prettier stylelint angular-testing-library codelyzer jasmine-spec-reporter ts-node tslint @types/jest @angular-devkit/build-angular
echo 'Removing Karma...'
yarn remove karma karma-chrome-launcher karma-coverage karma-jasmine karma-jasmine-html-reporter

cd ../ags-angular-init

echo 'Rewriting package.json...'
python3 ./scripts/package.json.py $projectName

echo 'Creating proxy config...'
touch ../$projectName/proxy.dev.config.json
python3 ./scripts/dev-proxy.py $projectName

echo 'Creating stylelintrc...'
touch ../$projectName/.stylelintrc
python3 ./scripts/stylelint.py $projectName

echo 'Rewriting readme...'
python3 ./scripts/readme.py $projectName

echo 'Setting up testing...'
touch ../$projectName/src/setup-jest.ts
rm ../$projectName/src/test.ts
rm ../$projectName/karma.conf.js
python3 ./scripts/test-files.py $projectName
python3 ./scripts/angular.json.py $projectName

echo 'Setting up styling...'
python3 ./scripts/style-files.py $projectName

echo 'Creating folders and starter components...'
python3 ./scripts/copy-files.py $projectName
mkdir ../$projectName/src/app/guards
mkdir ../$projectName/src/app/models

python3 ./scripts/app.module.py $projectName

cd ../$projectName
git add .
git commit -m "initial commit"

echo 'Enjoy your new project :D'
exit
