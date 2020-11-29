import os

from profile_readme.generator import ProfileGenerator


def test_build(tmpdir):
    teplate_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(teplate_path, 'w') as fp:
        fp.write('Hello, World!')

    generator = ProfileGenerator(teplate_path=teplate_path, output_path=output_path)
    generator.render()

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'


def test_build_with_context(tmpdir):
    teplate_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(teplate_path, 'w') as fp:
        fp.write('Hello, {{ name }}!')

    generator = ProfileGenerator(teplate_path=teplate_path, output_path=output_path, context={'name': "World"})
    generator.render()

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'


def test_build_with_filters(tmpdir):
    teplate_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(teplate_path, 'w') as fp:
        fp.write('Hello, {{ "Joe"|foo }}!')

    generator = ProfileGenerator(teplate_path=teplate_path, output_path=output_path, filters={'foo': lambda x: "Foo"})
    generator.render()

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == "Hello, Foo!"
