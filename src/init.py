import os

import click


BASE_TEMPLATE = """\
<h2>Hi there 👋</h2>

<!-- This is just the base template, feel free to change it. -->
"""

PROFILE_SUMMARY_TEMPLATE = """\
<p>
    I'm a developer based in <i>{{ USER.location }}</i>
    and I'm on GitHub since {{ USER.created_at|datetimeformat('%Y') }}
    with <a href="https://github.com/{{ USER.login }}?tab=repositories">{{ USER.public_repos }} public repositories</a>
    and <a href="https://github.com/{{ USER.login }}?tab=followers">{{ USER.followers }} followers</a>.
</p>
"""

WEBSITE_TEMPLATE = """\
{% if USER.blog %}
    <p>Website: <a href="{{ USER.blog }}">{{ USER.blog }}<a></p>
{% endif %}
"""

TOP_LANGUAGES_TEMPLAGE = """\
<h3>Top Languages</h3>

<ul>
{% for language in TOP_LANGUAGES %}
    <li>{{ language.name }}: {{ language.percentage }}%</li>
{% endfor %}
</ul>
"""

POPULAR_REPOS_TEMPLATE = """\
<h3>Popular Repositories</h3>

<ul>
{% for repo in POPULAR_REPOS %}
    <li>
        <a href="{{ repo.html_url }}">{{ repo.name }}</a>
        {% if repo.language %}
            (<i>{{ repo.language }}</i>)
        {% endif %}
    </li>
{% endfor %}
</ul>
"""

GISTS_TEMPLATE = """\
{% if GISTS %}
<h3>Pupular Gists</h3>

<ul>
{% for gist in GISTS[:5] %}
    {% if gist.description %}
        <li><a href="{{ gist.html_url }}">{{ gist.description }}</a></li>
    {% endif %}
{% endfor %}
</ul>
{% endif %}
"""

ORGANIZATIONS_TEMPLATE = """\
{% if ORGS %}
<h3>Organizations</h3>

<ul>
{% for org in ORGS %}
    <li>{{ org.login }} {%- if org.description %}: {{ org.description }} {%- endif %}</li>
{% endfor %}
</ul>
{%- endif %}
"""

TIME_STAMP_TEMPLATE = """\
<p><strong>Updated</strong>: <i>{{ TIME_STAMP|datetimeformat }}</i></p>
"""

GITHUB_ACTION = """\
name: README

on:
  push:
    branches:
      - master
  schedule:
    - cron: '0 11 * * *'

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Get the code
        uses: actions/checkout@master
        with:
          fetch-depth: 1
      - name: Update README.md
        run: |
          python3 -m pip install -U git+https://github.com/Robert-96/profile-readme.git
          python3 -m profile-readme update
      - name: Deploy
        run: |
          git config user.name "${GITHUB_ACTOR}"
          git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
          git add .
          git commit -am "Update README.md from GitHub action"
          git push --all -f https://${{ secrets.GITHUB_TOKEN }}@github.com/${GITHUB_REPOSITORY}.git
"""


def init_template(file):
    content = [BASE_TEMPLATE]
    prompts = [
        ("profile summary", PROFILE_SUMMARY_TEMPLATE),
        ("website", WEBSITE_TEMPLATE),
        ("top languages", TOP_LANGUAGES_TEMPLAGE),
        ("popular repos", POPULAR_REPOS_TEMPLATE),
        ("gists", GISTS_TEMPLATE),
        ("organizations", ORGANIZATIONS_TEMPLATE)
    ]

    for message, template in prompts:
        text = "  * Do you want to add your {}?".format(click.style(message, fg="yellow", bold=True))

        if click.confirm(text):
            content.append(template)

    content.append(TIME_STAMP_TEMPLATE)
    click.echo()

    with open(file, 'w') as fp:
        fp.write("\n".join(content))


def init_actions():
    actions_dir = ".github/workflows"

    if not os.path.exists(actions_dir):
        os.makedirs(actions_dir)

    with open(os.path.join(actions_dir, "readme.yml"), 'w') as fp:
        fp.write(GITHUB_ACTION)

    click.secho("  GitHub action succesfuly generated.", fg="green")
    click.echo()


def init_project(file):
    if click.confirm("Generate README template: ", default=True):
        init_template(file)
    else:
        click.echo()

    if click.confirm("Generate GitHub action: ", default=True):
        init_actions()
    else:
        click.echo()
