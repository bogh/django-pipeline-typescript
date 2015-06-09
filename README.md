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
