import os

from profile_readme.generator import ProfileGenerator


def test_build(tmpdir):
    template_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(template_path, 'w') as fp:
        fp.write('Hello, World!')

    ProfileGenerator.render(template_path=template_path, output_path=output_path)

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'


def test_build_with_context(tmpdir):
    template_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(template_path, 'w') as fp:
        fp.write('Hello, {{ name }}!')

    ProfileGenerator.render(template_path=template_path, output_path=output_path, context={'name': "World"})

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == 'Hello, World!'


def test_build_with_filters(tmpdir):
    template_path = os.path.join(tmpdir, 'TEMPLATE-REAME.md')
    output_path = os.path.join(tmpdir, 'README.md')

    with open(template_path, 'w') as fp:
        fp.write('Hello, {{ "Joe"|foo }}!')

    ProfileGenerator.render(template_path=template_path, output_path=output_path, filters={'foo': lambda x: "Foo"})

    with open(output_path, 'r') as fp:
        readme_content = fp.read()

    assert readme_content == "Hello, Foo!"
