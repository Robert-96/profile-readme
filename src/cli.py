import logging

import click
from click_help_colors import HelpColorsGroup
from dotenv import load_dotenv

from .utils import config_logger
from .init import init_project
from .template import render_readme


config_logger()
logger = logging.getLogger()

load_dotenv()


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
)
def cli():
    """A CLI tool for generating a GitHub profile README."""


@cli.command()
@click.option("--template", type=click.Path(exists=False, dir_okay=False, writable=True),
              default="README-TEMPLATE.md", help="The ouptut path for the README template file.")
def init(template):
    """Initiate a new profile README project."""

    click.secho("Intiate a new profile README project...\n", bold=True, fg="green")

    init_project(template)

    click.secho("The profile README project was successfully created!", bold=True, fg="green")


@cli.command()
@click.option("--template", envvar='TEMPLATE', type=click.Path(exists=False, dir_okay=False, writable=True),
              default="README-TEMPLATE.md", show_default=True, help="The path of the README template file.")
@click.option("--readme", envvar='README', type=click.Path(exists=False, dir_okay=False, writable=True),
              default="README.md", show_default=True, help="The ouptut path for the README file.")
@click.option("--user", envvar='GITHUB_ACTOR', type=str, default="octocat", show_default=True,
              help="The GitHub username.")
def render(template, readme, user):
    """Render the README template and save it in a README file."""

    click.secho("Render the '{}' template...\n".format(template), bold=True, fg="green")

    width = max(len(template), len(readme), len(user)) + 20
    click.secho("  TEMPLATE..........{}".format(click.style(template, fg="yellow", bold=True).rjust(width, ".")))
    click.secho("  README............{}".format(click.style(readme, fg="yellow", bold=True).rjust(width, ".")))
    click.secho("  USER..............{}".format(click.style(user, fg="yellow", bold=True).rjust(width, ".")))
    click.echo()

    render_readme(template, readme, user)
    click.secho("The '{}' was successfully updated!".format(readme), bold=True, fg="green")


if __name__ == "__main__":
    cli()
