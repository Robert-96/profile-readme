import os

from click.testing import CliRunner

from profile_readme.cli import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.exit_code == 0
    assert result.output != ''


def test_render(tmpdir):
    teplate_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(teplate_path, 'w') as fp:
        fp.write('Hello, World!')

    runner = CliRunner()
    runner.invoke(cli, [
        'render',
        '--template', teplate_path,
        '--output', output_path
    ])

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'


def test_render_quiet(tmpdir):
    teplate_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(teplate_path, 'w') as fp:
        fp.write('Hello, World!')

    runner = CliRunner()
    result = runner.invoke(cli, [
        'render',
        '--template', teplate_path,
        '--output', output_path,
        '--quiet'
    ])

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'
    assert result.output == ''


def test_render_verbose(tmpdir):
    teplate_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(teplate_path, 'w') as fp:
        fp.write('Hello, World!')

    runner = CliRunner()
    result = runner.invoke(cli, [
        'render',
        '--template', teplate_path,
        '--output', output_path,
        '--verbose'
    ])

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'
    assert result.output != ''
