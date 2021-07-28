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
    // "src/**/*.ts"
  ],
  "exclude": [
    "src/test.ts",
    "src/**/*.spec.ts"
  ]
}
'''

ts_config_spec_content = '''
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "emitDecoratorMetadata": true,
    "outDir": "./out-tsc/spec",
    "types": [
      "jasmine",
      "node"
    ]
  },
  "files": [
    "src/test.ts",
    "src/polyfills.ts"
  ],
  "include": [
    "src/**/*.spec.ts",
    "src/**/*.d.ts"
  ]
}
'''

main_ts_content = '''

const mock = () => {
  let storage: any = {};
  return {
    getItem: (key: any) => (key in storage ? storage[key] : null),
    setItem: (key: any, value: any) => (storage[key] = value || ''),
    removeItem: (key: any) => delete storage[key],
    clear: () => (storage = {})
  };
};

Object.defineProperty(window, 'localStorage', { value: mock() });
Object.defineProperty(window, 'sessionStorage', { value: mock() });
Object.defineProperty(window, 'getComputedStyle', {
  value: () => ['-webkit-appearance']
});
// Used to fix the ReferenceError: CSS is not defined ERROR
Object.defineProperty(window, 'CSS', { value: mock() });
// Suppresses console warning from Materia
console.warn = () => {
  return;
};

Object.defineProperty(window, 'SVGElement', { value: Element });
/**
 * ISSUE: https://github.com/angular/material2/issues/7101
 * Workaround for JSDOM missing transform property
 */
Object.defineProperty(document.body.style, 'transform', {
  value: () => {
    return {
      enumerable: true,
      configurable: true
    };
  }
});

/**
 * Fixes Material SnackBar window binding
 */
Object.defineProperty(window, 'matchMedia', {
  value: () => {
    return window.matchMedia.bind(window);
  }
});
'''

setup_jest_content = '''
import 'jest-preset-angular';
import './jest-global-mocks';
'''

with open(package_file_path + '/tsconfig.app.json', 'r+') as f:
  f.seek(0)
  f.write(ts_config_app_content)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/tsconfig.spec.json', 'r+') as f:
  f.seek(0)
  f.write(ts_config_spec_content)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/src/test-global-mocks.ts', 'r+') as f:
  f.seek(0)
  f.write(main_ts_content)
  f.write('\n')
  f.truncate()

with open(package_file_path + '/src/setup-jest.ts', 'r+') as f:
  f.seek(0)
  f.write(setup_jest_content)
  f.write('\n')
  f.truncate()


