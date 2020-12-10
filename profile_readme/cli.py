"""A CLI tool for generating a GitHub profile README using the Jinja2 template engine."""

import click
from click_help_colors import HelpColorsGroup

from .init import init_project
from .generator import get_github_context, ProfileGenerator


CONTEXT_SETTINGS = dict(help_option_names=["--help", "-h"])


@click.group(
    context_settings=CONTEXT_SETTINGS,
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
)
@click.version_option(None, "--version", "-v", prog_name="profile-readme")
def cli():
    """A CLI tool for generating a GitHub profile README."""


@cli.command()
@click.option("--template", type=click.Path(exists=False, dir_okay=False, writable=True),
              default="README-TEMPLATE.md", help="The ouptut path for the README template file.")
def init(template):
    """Initiate a new profile README project using the Jinja2 template engine."""

    click.secho("Intiate a new profile README project...\n", bold=True, fg="green")

    init_project(template)

    click.secho("The profile README project was successfully created!", bold=True, fg="green")


@cli.command()
@click.option("--template", envvar='TEMPLATE', type=click.Path(exists=False, dir_okay=False, writable=True),
              default="README-TEMPLATE.md", show_default=True, help="The path of the README template file.")
@click.option("--readme", "--output", envvar='README', type=click.Path(exists=False, dir_okay=False, writable=True),
              default="README.md", show_default=True, help="The ouptut path for the README file.")
@click.option("--user", envvar='GITHUB_ACTOR', type=str, default="octocat", show_default=True,
              help="The GitHub username.")
@click.option("--verbose/--quiet", default=True, show_default=True,
              help="Make the operation more talkative.")
def render(template, readme, user, verbose):
    """Render the README template and save it in a README file."""

    if verbose:
        click.secho("Render the '{}' template...\n".format(template), bold=True, fg="green")

        width = max(len(template), len(readme), len(user)) + 20
        click.secho("  TEMPLATE..........{}".format(click.style(template, fg="yellow", bold=True).rjust(width, ".")))
        click.secho("  README............{}".format(click.style(readme, fg="yellow", bold=True).rjust(width, ".")))
        click.secho("  USER..............{}".format(click.style(user, fg="yellow", bold=True).rjust(width, ".")))
        click.echo()

    ProfileGenerator.render(template_path=template, output_path=readme, context=get_github_context(user))

    if verbose:
        click.secho("The '{}' was successfully updated!".format(readme), bold=True, fg="green")


if __name__ == "__main__":
    cli()
