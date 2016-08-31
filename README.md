# django-pipeline-typescript
Pipeline compiler for Typescript

#### Installation

You need django-pipeline, this library contains only the compiler for typescript and you also need to install typescript compiler using node package manager:

[Django Pipeline](http://django-pipeline.readthedocs.org/en/latest/index.html)

[NodeJS & NPM](https://nodejs.org/)

``` npm install -g typescript```

```pip install django-pipeline-typescript```

Add the compiler to pipeline configuration:

```
PIPELINE_COMPILERS = (
  'pipeline_typescript.compilers.TypescriptCompiler',
)
```

#### Using a local typescript install

If you don't want to install the `typescript` dependency globally, you can install it within a specific project:

	npm install --save-dev typescript

Then, tell django-pipeline where the executable is:

	# In settings.py
	PIPELINE_TYPESCRIPT_BINARY = 'node_modules/.bin/tsc'

#### The compiler is erroring out with "exit code 2"

For some reason the most recent versions of `tsc` errors out with "exit code 2"

	pipeline.exceptions.CompilerError: ['node_modules/.bin/tsc', '', '-out', '/some/django/dir/static/ts/main.js', '/some/django/dir/static/ts/main.ts'] exit code 2
	b''

Even more bizarre, the compiled Javascript file _is_ being output, so this doesn't necessarily indicate an issue with the TypeScript code itself...

For some reason setting an argument (like `--diagnostics`) allows the `collectstatic` command to finish without issue:

	# In settings.py
	PIPELINE_TYPESCRIPT_ARGUMENTS = '--diagnostics'

This appears to be related to [this Github issue](https://github.com/Microsoft/TypeScript/issues/8186) on the Microsoft/TypeScript repo.