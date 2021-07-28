#!/bin/sh

cd $(dirname $0)

# Get user to define the project name
read  -p "Project Name:" projectName

# Update Angular CLI
echo "Updating global Angular CLI to the latest version..."
npm install -g @angular/cli@latest

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
echo 'Installing additional dependencies...'
yarn add @angular/router @ngrx/store @ngrx/router @ngrx/effects @ngrx/router-store ngrx-store-localstorage normalize-scss rxjs @angular/cdk ngrx-store-freeze @ngrx/store-devtools @angular/material
echo 'Installing additional dev dependencies...'
yarn add -D husky typescript prettier stylelint angular-testing-library codelyzer jasmine-spec-reporter ts-node tslint
echo 'Removing Karma...'
ng add @briebug/jest

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
touch ../$projectName/src/test-global-mocks.ts
python3 ./scripts/test-files.py $projectName

echo 'Setting up styling...'
python3 ./scripts/style-files.py $projectName

echo 'Creating folders and starter components...'
python3 ./scripts/copy-files.py $projectName
mkdir ../$projectName/src/app/guards
mkdir ../$projectName/src/app/models

cd ../$projectName/src/app/components
ng g c text-box
cd ../containers
ng g c home
ng g c not-found

cd ../../../../ags-angular-init
python3 ./scripts/app.module.py $projectName

cd ../$projectName
git add .
git commit -m "initial commit" --no-verify

echo 'Enjoy your new project :D'
exit 1
