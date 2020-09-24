import json
import logging
from collections import defaultdict

import requests
import requests_cache

from .utils import config_logger


config_logger()
logger = logging.getLogger(__name__)

requests_cache.install_cache('github')

BASE_URL = 'https://api.github.com'


def get_user(user):
    user_raw = requests.get('{}/users/{}'.format(BASE_URL, user))
    return user_raw.json()


def _get_repos_page(user, page=1, per_page=100):
    repos_raw = requests.get('{}/users/{}/repos?page={}&per_page={}'.format(BASE_URL, user, page, per_page))
    return repos_raw.json()


def _get_repos(user, page=1, prev_data=None, per_page=100):
    data = prev_data if prev_data else []

    repos = _get_repos_page(user, page=page, per_page=per_page)
    data.extend(repos)

    if len(repos) < per_page:
        return data
    else:
        return _get_repos(user, page=page + 1, prev_data=data, per_page=per_page)


def get_repos(user):
    return _get_repos(user, page=1, prev_data=None, per_page=100)


def _popular_repo_key(repo):
    return repo.get('fork_count', 0) + repo.get('stargazers_count', 0) + repo.get('watchers_count', 0)


def get_popular_repos(user):
    repos = [repo for repo in get_repos(user) if repo.get('name') != user]
    repos.sort(key=_popular_repo_key, reverse=True)

    return repos[:5]


def get_gist(id):
    gist_raw = requests.get('{}/gists/{}'.format(BASE_URL, id))
    return gist_raw.json()


def get_gists(user):
    gists_raw = requests.get('{}/users/{}/gists'.format(BASE_URL, user))
    return gists_raw.json()


def _get_languages(user):
    repos = get_repos(user)

    total = 0
    languages = defaultdict(int)

    for repo in repos:
        if repo['language'] and not repo['fork']:
            language = repo['language']

            logger.info("{}: {}".format(
                repo['name'],
                language
            ))

            languages[language] += 1
            total += 1

    return total, languages


def _compute_top_languages(total, languages):
    top_languages = []

    for language, value in languages.items():
        percentage = round((value / total) * 100, 2)

        if percentage:
            top_languages.append({
                'name': language,
                'percentage': percentage
            })

    top_languages.sort(key=lambda language: language.get('percentage', 0), reverse=True)
    logger.info(json.dumps(top_languages, sort_keys=True, indent=4))

    return top_languages


def get_top_languages(user):
    total, languages = _get_languages(user)
    return _compute_top_languages(total, languages)


def get_orgs(user):
    orgs_raw = requests.get('{}/users/{}/orgs'.format(BASE_URL, user))
    return orgs_raw.json()


def _get_issues_page(user, page=1, per_page=100):
    issues_raw = requests.get('{}/search/issues?q=type:pr+is:merged+author:{}&page={}&per_page={}'.format(
        BASE_URL, user, page, per_page
    ))
    return issues_raw.json().get('items')


def _get_issues(user, page=1, prev_data=None, per_page=100):
    data = prev_data if prev_data else []

    issues = _get_issues_page(user, page=page, per_page=per_page)
    data.extend(issues)

    if len(issues) < per_page:
        return data
    else:
        return _get_issues(user, page=page + 1, prev_data=data, per_page=per_page)


def get_issues(user):
    return _get_issues(user, page=1, prev_data=None, per_page=100)


def _get_contributions(user):
    issues = get_issues(user)
    contributions = defaultdict(int)

    for issue in issues:
        contributions[issue['repository_url']] += 1

    logger.info(json.dumps(contributions, indent=4))
    return contributions


def _compute_top_contributions(user, contributions):
    top_contributions = []

    for url, count in contributions.items():
        top_contributions.append({
            'url': url.replace('https://api.github.com/repos/', 'https://github.com/'),
            'commits_url': 'https://api.github.com/repos/commits?author={}'.format(user),
            'name': url.replace('https://api.github.com/repos/', ''),
            'count': count
        })

    top_contributions.sort(key=lambda contribution: contribution.get('count', 0), reverse=True)
    logger.info(json.dumps(top_contributions, sort_keys=True, indent=4))

    return top_contributions


def get_contributions(user):
    contributions = _get_contributions(user)
    return _compute_top_contributions(user, contributions)
