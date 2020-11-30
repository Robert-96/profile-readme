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
        user (:obj:`str`): The GitHub user name.
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
    """Simple Jinja2 profile README generator.

    Args:
        template_path (:obj:`str`): A string representing the path of the template.
            Defaults to 'README-TEMPLATE.md'.
        output_path (:obj:`str`): A string representing the output path of the README.md file.
            Defaults to 'README.md'.
        context (:obj:`dict`): A dictonary of data to supply to the template.
            Defaults to None.
        filters (:obj:`dict`): A dictionary of filters to add to the Environment.
            Defaults to None.
    """

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

        return dict(**self.context, **{
            'TIME_STAMP': get_time_stamp()
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

    @classmethod
    def render(cls, teplate_path="README-TEMPLATE.md", output_path="README.md", context=None, filters=None):
        """Reander the profile README file.

        Args:
            template_path (:obj:`str`): A string representing the path of the template.
                Defaults to 'README-TEMPLATE.md'.
            output_path (:obj:`str`): A string representing the output path of the README.md file.
                Defaults to 'README.md'.
            context (:obj:`dict`): A dictonary of data to supply to the template.
                Defaults to None.
            filters (:obj:`dict`): A dictionary of filters to add to the Environment.
                Defaults to None.
        """

        generator = cls(teplate_path=teplate_path, output_path=output_path, context=context, filters=filters)
        generator.render_template()
