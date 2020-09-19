from profile_readme.template import render_template, update_readme, render_readme


REPOS = [
  {
    "name": "2048",
    "full_name": "Robert-96/2048",
    "html_url": "https://github.com/Robert-96/2048",
    "description": "2048 is played on a gray 4×4 grid, with numbered tiles that slide when a player moves them using the four arrow keys.",
    "fork": False,
    "created_at": "2020-09-08T23:26:11Z",
    "updated_at": "2020-09-09T17:18:56Z",
    "pushed_at": "2020-09-09T17:20:59Z",
    "homepage": "https://robert-96.github.io/2048",
    "size": 2672,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "JavaScript",
    "forks_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit",
      "node_id": "MDc6TGljZW5zZTEz"
    },
    "forks": 0,
    "watchers": 0,
  },
  {
    "name": "ember-build-time-data",
    "full_name": "Robert-96/ember-build-time-data",
    "html_url": "https://github.com/Robert-96/ember-build-time-data",
    "description": "An Ember addon to help you insert JSON data into your application at build time.",
    "fork": False,
    "created_at": "2020-07-14T20:07:33Z",
    "updated_at": "2020-08-25T15:34:30Z",
    "pushed_at": "2020-08-21T22:12:37Z",
    "homepage": "https://robert-96.github.io/ember-build-time-data/",
    "size": 1236,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "JavaScript",
    "forks_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit",
      "node_id": "MDc6TGljZW5zZTEz"
    },
    "forks": 0,
    "watchers": 0,
  },
  {
    "name": "empty",
    "full_name": "Robert-96/empty",
    "html_url": "https://github.com/Robert-96/empty",
    "description": None,
    "fork": False,
    "created_at": "2020-01-30T20:51:27Z",
    "updated_at": "2020-01-30T20:51:27Z",
    "pushed_at": "2020-01-30T20:51:29Z",
    "homepage": None,
    "size": 0,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": None,
    "forks_count": 0,
    "license": None,
    "forks": 0,
    "watchers": 0,
  }
]

OPTIONS = {
    'REPOS': REPOS,
}


def test_empty_template():
    assert render_template('', **OPTIONS) == ''


def test_repos_template():
    template = '{% for repo in REPOS %}{{ repo.name }}{% endfor %}'
    expected = ''.join([repo.get('name') for repo in REPOS])

    assert render_template(template, **OPTIONS).strip() == expected