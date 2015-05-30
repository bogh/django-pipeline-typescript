from __future__ import unicode_literals

from django.conf import settings as _settings
from pipeline.compilers import CompilerBase

DEFAULTS = {
    'PIPELINE_TYPESCRIPT_BINARY': '/usr/bin/env tsc',
    'PIPELINE_TYPESCRIPT_ARGUMENTS': ''
}


def get_setting(name):
    if hasattr(_settings, name):
        return getattr(_settings, name)
    return DEFAULTS[name]


class TypescriptCompiler(CompilerBase):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.ts')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled

        command = "{command} {arguments} -out {outfile} {infile}".format(
            command=get_setting('PIPELINE_TYPESCRIPT_BINARY'),
            arguments=get_setting('PIPELINE_TYPESCRIPT_ARGUMENTS'),
            infile=infile,
            outfile=outfile)
        return self.execute_command(command)
