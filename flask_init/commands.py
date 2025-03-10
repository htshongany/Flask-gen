# flask_init/commands.py

import click
from flask.cli import AppGroup
from flask_init.src import project_creator, app_creator

init_cli = AppGroup('init', help="Initialization commands for your Flask project.")

@init_cli.command('project')
@click.argument("name")
@click.argument("path", default=".")
def init_project(name, path):
    """Initialize a complete Flask project."""
    project_creator.init_project(name, path)
    click.echo(f"Project '{name}' has been initialized at {path}.")

@init_cli.command('app')
@click.argument("name")
@click.argument("path", default=".")
def init_app(name, path):
    """Initialize a new Flask application (blueprint)."""
    app_creator.init_app(name, path)
    click.echo(f"App '{name}' has been initialized at {path}.")
