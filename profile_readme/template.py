import logging

from jinja2 import Environment

from .utils import config_logger, datetimeformat, get_time_stamp
from .github import get_user, get_repos, get_popular_repos, get_top_languages, get_gists, get_orgs, get_contributions


config_logger()
logger = logging.getLogger(__name__)


def render_template(template, **options):
    env = Environment(trim_blocks=True, lstrip_blocks=True)
    env.filters['datetimeformat'] = datetimeformat

    template = env.from_string(template)
    return template.render(options)


def update_readme(template, readme, **options):
    with open(template, 'r') as fp:
        template_content = fp.read()

    readme_content = render_template(template_content, **options)

    with open(readme, 'w') as fp:
        fp.write(readme_content)


def render_readme(template, readme, user):
    update_readme(template, readme, **{
        'TIME_STAMP': get_time_stamp(),
        'USER': get_user(user),
        'TOP_LANGUAGES': get_top_languages(user),
        'REPOS': get_repos(user),
        'POPULAR_REPOS': get_popular_repos(user),
        'GISTS': get_gists(user),
        'ORGS': get_orgs(user),
        'CONTRIBUTIONS': get_contributions(user)
    })
