"""Simple GitHub profile README generator based on Jinja2."""

import logging

from jinja2 import Environment

from .utils import config_logger, datetimeformat, get_time_stamp
from .github import get_user, get_repos, get_popular_repos, get_top_languages, get_gists, get_orgs, get_contributions


config_logger()
logger = logging.getLogger(__name__)


def get_github_context(user):
    """Get the data from the GitHub API for the template.

    Args:
        user (`str`): The user name of the GitHub user.
    """

    return {
        'USER': get_user(user),
        'TOP_LANGUAGES': get_top_languages(user),
        'REPOS': get_repos(user),
        'POPULAR_REPOS': get_popular_repos(user),
        'GISTS': get_gists(user),
        'ORGS': get_orgs(user),
        'CONTRIBUTIONS': get_contributions(user)
    }


class ProfileGenerator:
    """Simple Jinja2 profile README generator."""

    def __init__(self, teplate_path="README-TEMPLATE.md", output_path="README.md", context=None, filters=None):
        self.teplate_path = teplate_path
        self.output_path = output_path

        self.context = context or {}
        self.filters = filters or {}

        self.env = Environment(
            trim_blocks=True,
            lstrip_blocks=True
        )
        self.env.filters['datetimeformat'] = datetimeformat
        self.env.filters.update(self.filters)

    def get_context(self):
        """Get the context for the template."""

        return self.context.update({
            'TIME_STAMP': get_time_stamp(),
        })

    def get_template(self):
        """Get a :class:`jinja2.Template` from the environment."""

        with open(self.teplate_path, 'r') as fp:
            template_content = fp.read()

        return self.env.from_string(template_content)

    def render_template(self):
        """Render the Jinja2 templates."""

        template = self.get_template()
        template.stream(self.get_context()).dump(self.output_path)

    def render(self):
        """Reander the profile README file."""

        self.render_template()
