import click
from mark.compiler.compiler import compile as mark_compile
from mark.dev.watcher import watch as mark_watch
from mark.config.init_config import init_config as mark_init_config
from mark.config.load_config import load_config


# @click.option('-o', '--output', 'outfile')
@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def watch(filepath: str):
    load_config()
    mark_watch(filepath)


# @click.option('-o', '--output', 'outfile')
@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def compile(filepath: str):
    load_config()
    mark_compile(filepath)


@click.command()
def init():
    mark_init_config()


@click.group()
def cli():
    pass


commands = [compile, watch, init]
for command in commands:
    cli.add_command(command)
