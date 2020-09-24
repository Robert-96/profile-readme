import pytest

from profile_readme.github import _compute_top_languages


@pytest.mark.parametrize(
    "total, languages, expected",
    [
        (100, {'Py': 0}, []),
        (100, {'Py': 50}, [{'name': 'Py', 'percentage': 50}]),
        (100, {'Py': 100}, [{'name': 'Py', 'percentage': 100}]),
        *[(100, {'Py': x}, [{'name': 'Py', 'percentage': x}]) for x in range(1, 100)],
        (200, {'Py': 0}, []),
        (200, {'Py': 100}, [{'name': 'Py', 'percentage': 50}]),
        (200, {'Py': 200}, [{'name': 'Py', 'percentage': 100}]),
        *[(200, {'Py': 2 * x}, [{'name': 'Py', 'percentage': x}]) for x in range(1, 100)],
        (100, {'Py': 100, 'JS': 0}, [{'name': 'Py', 'percentage': 100}]),
        (100, {'Py': 0, 'JS': 100}, [{'name': 'JS', 'percentage': 100}]),
        (100, {'Py': 50, 'JS': 50}, [{'name': 'Py', 'percentage': 50}, {'name': 'JS', 'percentage': 50}]),
        (200, {'Py': 100, 'JS': 100}, [{'name': 'Py', 'percentage': 50}, {'name': 'JS', 'percentage': 50}]),
    ]
)
def test_compute_top_languages(total, languages, expected):
    top_languages = _compute_top_languages(total, languages)

    assert top_languages == expected
