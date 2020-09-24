import json

from profile_readme.template import render_template, update_readme, render_readme


OPTIONS = {
}

with open('tests/data/user.json', 'r') as fp:
    OPTIONS['USER'] = json.loads(fp.read())

with open('tests/data/top-languages.json', 'r') as fp:
    OPTIONS['TOP_LANGUAGES'] = json.loads(fp.read())

with open('tests/data/repos.json', 'r') as fp:
    OPTIONS['REPOS'] = json.loads(fp.read())

with open('tests/data/popular-repos.json', 'r') as fp:
    OPTIONS['POPULAR_REPOS'] = json.loads(fp.read())

with open('tests/data/gists.json', 'r') as fp:
    OPTIONS['GISTS'] = json.loads(fp.read())

with open('tests/data/orgs.json', 'r') as fp:
    OPTIONS['ORGS'] = json.loads(fp.read())

with open('tests/data/contributions.json', 'r') as fp:
    OPTIONS['CONTRIBUTIONS'] = json.loads(fp.read())


def test_empty_template():
    assert render_template('', **OPTIONS) == ''


def test_user_template():
    template = '{{ USER.login }}'
    expected = OPTIONS['USER']['login']

    assert render_template(template, **OPTIONS).strip() == expected


def test_top_languages_template():
    template = '{% for language in TOP_LANGUAGES %}{{ language.name }}{% endfor %}'
    expected = ''.join([language.get('name') for language in OPTIONS['TOP_LANGUAGES']])

    assert render_template(template, **OPTIONS).strip() == expected


def test_repos_template():
    template = '{% for repo in REPOS %}{{ repo.name }}{% endfor %}'
    expected = ''.join([repo.get('name') for repo in OPTIONS['REPOS']])

    assert render_template(template, **OPTIONS).strip() == expected


def test_popular_repos_template():
    template = '{% for repo in REPOS %}{{ repo.name }}{% endfor %}'
    expected = ''.join([repo.get('name') for repo in OPTIONS['REPOS']])

    assert render_template(template, **OPTIONS).strip() == expected


def test_gists_template():
    template = '{% for gist in GISTS %}{{ gist.id }}{% endfor %}'
    expected = ''.join([gist.get('id') for gist in OPTIONS['GISTS']])

    assert render_template(template, **OPTIONS).strip() == expected


def test_orgs_template():
    template = '{% for org in ORGS %}{{ org.login }}{% endfor %}'
    expected = ''.join([org.get('login') for org in OPTIONS['ORGS']])

    assert render_template(template, **OPTIONS).strip() == expected


def test_orgs_contributions():
    template = '{% for contribution in CONTRIBUTIONS %}{{ contribution.name }}{% endfor %}'
    expected = ''.join([contribution.get('name') for contribution in OPTIONS['CONTRIBUTIONS']])

    assert render_template(template, **OPTIONS).strip() == expected
