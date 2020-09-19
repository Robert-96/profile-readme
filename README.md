# profile-readme

A CLI tool for generating a GitHub profile README.

It uses [Jinja2](https://jinja.palletsprojects.com/) as a template engine and it provides data from the GitHub API to the template.

## Installation

Use the following command to install `profile-readme`:

```
$ python3 -m pip install profile-readme
```

### Living on the edge

If you want to work with the latest code before it’s released, install or update the code from the `master` branch:

```
$ python3 -m pip install -U git+https://github.com/Robert-96/profile-readme.git
```

## Quickstart

Use the `init` command to generate a new project with an example template:

```
$ profile-readme init
```

Use the `render` command to update your `README.md` file:

```
$ profile-readme render
```

## License

This project is licensed under the [MIT License](LICENSE).