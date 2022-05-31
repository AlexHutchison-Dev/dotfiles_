#!/bin/python3
import click
import add_file


@click.group()
def cli():
    """
    A cli program for managing dotfiles
    """
    pass


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def add(filename):
    add_file.AddFile(filename)


cli.add_command(add)
