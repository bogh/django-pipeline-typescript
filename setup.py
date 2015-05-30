from distutils.core import setup

setup(
  name='django-pipeline-typescript',
  packages=['pipeline_typescript'],
  version='0.1',
  description='Django Pipeline Compiler for Typescript',
  author='Bogdan I. Bursuc',
  author_email='bogdanbursuc86@gmail.com',
  url='https://github.com/Bogh/django-pipeline-typescript',  # use the URL to the github repo
  # download_url='https://github.com/peterldowns/mypackage/tarball/0.1',  # I'll explain this in a second
  keywords=['pipeline', 'assets', 'typescript'],  # arbitrary keywords
  classifiers=[
    "Programming Language :: Python :: 2.7",
    "Framework :: Django",
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
  ],
  install_requires=[
    'django_pipeline>=1.4.0'
  ]
)
