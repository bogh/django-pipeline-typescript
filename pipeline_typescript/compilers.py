from __future__ import unicode_literals

from django.conf import settings as _settings
from pipeline.compilers import SubProcessCompiler

DEFAULTS = {
    'PIPELINE_TYPESCRIPT_BINARY': ('/usr/bin/env', 'tsc'),
    'PIPELINE_TYPESCRIPT_ARGUMENTS': (None,)
}


class TypescriptCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, path):
        return path.endswith('.ts')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return
        command = (
            settings.get('PIPELINE_TYPESCRIPT_BINARY',
                         DEFAULTS["PIPELINE_TYPESCRIPT_BINARY"]),
            settings.get('PIPELINE_TYPESCRIPT_ARGUMENTS',
                         DEFAULTS["PIPELINE_TYPESCRIPT_ARGUMENTS"]),
            infile,
            )
        return self.execute_command(command)
