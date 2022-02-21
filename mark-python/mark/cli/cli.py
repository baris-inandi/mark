import click
from mark.compiler.compiler import compile as mark_compile
from mark.dev.watcher import watch as mark_watch


# @click.option('-o', '--output', 'outfile')
@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def watch(filepath: str):
    mark_watch(filepath)


# @click.option('-o', '--output', 'outfile')
@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def compile(filepath: str):
    mark_compile(filepath)


@click.group()
def cli():
    pass


commands = [compile, watch]
for command in commands:
    cli.add_command(command)
