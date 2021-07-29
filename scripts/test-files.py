import os, sys

project_name = sys.argv[1]
package_file_path = '../' + project_name

ts_config_app_content = '''
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/app",
    "types": []
  },
  "files": [
    "src/main.ts",
    "src/polyfills.ts"
  ],
  "include": [
    "src/**/*.d.ts"
  ]
}
'''

ts_config_spec_content = '''
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/spec",
    "types": [
      "jest",
      "node"
    ]
  },
  "files": [
    "src/polyfills.ts"
  ],
  "include": [
    "src/**/*.spec.ts",
    "src/**/*.d.ts"
  ]
}
'''

ts_config = '''
{
  "compileOnSave": false,
  "compilerOptions": {
    "baseUrl": "./",
    "outDir": "./dist/out-tsc",
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "sourceMap": true,
    "declaration": false,
    "downlevelIteration": true,
    "experimentalDecorators": true,
    "esModuleInterop": true,
    "moduleResolution": "node",
    "importHelpers": true,
    "target": "es2017",
    "module": "es2020",
    "lib": [
      "es2018",
      "dom"
    ]
  },
  "angularCompilerOptions": {
    "enableI18nLegacyMessageIdFormat": false,
    "strictInjectionParameters": true,
    "strictInputAccessModifiers": true,
    "strictTemplates": true
  }
}
'''

setup_jest_content = '''
import 'jest-preset-angular/setup-jest';
'''

app_spec_test = '''
import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';

describe('AppComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [
        AppComponent
      ],
      imports: [RouterTestingModule]
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });
});
'''

with open(package_file_path + '/src/app/app.component.spec.ts', 'r+') as f:
  f.seek(0)
  f.write(app_spec_test)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/tsconfig.app.json', 'r+') as f:
  f.seek(0)
  f.write(ts_config_app_content)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/tsconfig.json', 'r+') as f:
  f.seek(0)
  f.write(ts_config)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/tsconfig.spec.json', 'r+') as f:
  f.seek(0)
  f.write(ts_config_spec_content)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/src/setup-jest.ts', 'r+') as f:
  f.seek(0)
  f.write(setup_jest_content)
  f.write('\n')
  f.truncate()


