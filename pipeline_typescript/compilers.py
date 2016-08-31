from __future__ import unicode_literals

from django.conf import settings as _settings
from pipeline.compilers import SubProcessCompiler

DEFAULTS = {
    'PIPELINE_TYPESCRIPT_BINARY': '/usr/bin/env tsc',
    'PIPELINE_TYPESCRIPT_ARGUMENTS': ''
}


def get_setting(name):
    if hasattr(_settings, name):
        return getattr(_settings, name)
    return DEFAULTS[name]


class TypescriptCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.ts')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        command = (
            get_setting('PIPELINE_TYPESCRIPT_BINARY'),
            get_setting('PIPELINE_TYPESCRIPT_ARGUMENTS'),
            '-out',
            outfile,
            infile
        )
        return self.execute_command(command)
