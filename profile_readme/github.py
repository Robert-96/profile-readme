import json
import logging
from collections import defaultdict

import requests
import requests_cache

from .utils import config_logger


config_logger()
logger = logging.getLogger(__name__)

requests_cache.install_cache('github')


def get_user(user):
    user_raw = requests.get('https://api.github.com/users/{}'.format(user))
    return user_raw.json()


def _get_repos_page(user, page=0, per_page=100):
    repos_raw = requests.get('https://api.github.com/users/{}/repos?page={}&per_page={}'.format(user, page, per_page))
    return repos_raw.json()


def _get_repos(user, page=0, data=None, per_page=100):
    if not data:
        data = []

    repos = _get_repos_page(user, page=page, per_page=per_page)
    data.extend(repos)

    if len(repos) < per_page:
        return data
    else:
        return _get_repos(user, page=page + 1, data=data, per_page=per_page)


def get_repos(user):
    return _get_repos(user, page=0, data=None, per_page=100)


def _popular_repo_key(repo):
    return repo.get('fork_count', 0) + repo.get('stargazers_count', 0) + repo.get('watchers_count', 0)


def get_popular_repos(user):
    repos = [repo for repo in get_repos(user) if repo.get('name') != user]
    repos.sort(key=_popular_repo_key, reverse=True)

    return repos[:5]


def get_gist(id):
    gist_raw = requests.get('https://api.github.com/gists/{}'.format(id))
    return gist_raw.json()


def get_gists(user):
    gists_raw = requests.get('https://api.github.com/users/{}/gists'.format(user))
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
    return top_languages


def get_top_languages(user):
    total, languages = _get_languages(user)
    top_languages = _compute_top_languages(total, languages)

    logger.info(json.dumps(top_languages, sort_keys=True, indent=4))

    return top_languages


def get_orgs(user):
    orgs_raw = requests.get('https://api.github.com/users/{}/orgs'.format(user))
    return orgs_raw.json()
