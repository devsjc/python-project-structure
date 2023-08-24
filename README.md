<h2 align="center">
MODERN PYTHON MICROSERVICE
<br>
<br>
Template for creating src-layout PEP628 compliant hexagonal python microservice.</h2>

<div align="center">

<a href="https://github.com/owner/package-name/graphs/contributors" alt="Contributors">
    <img src="https://img.shields.io/github/contributors/owner/package-name?style=for-the-badge" /></a>
<a href="https://github.com/owner/package-name/actions/workflows/ci.yml">
    <img alt="GitHub Workflow Status (with branch)" src="https://img.shields.io/github/actions/workflow/status/owner/package-name/ci.yml?branch=main&style=for-the-badge"></a>
<a href="https://github.com/owner/package-name/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc">
    <img src="https://img.shields.io/github/issues/owner/package-name?style=for-the-badge"></a>
<a href="https://github.com/owner/package-name/tags">
    <img alt="GitHub tag (latest SemVer pre-release)" src="https://img.shields.io/github/v/tag/openclimatefix/package-name?include_prereleases&sort=semver&style=for-the-badge"></a>
<a href="https://pypi.org/project/package-name">
    <img alt="PyPI tag (latest SemVer pre-release)" src="https://img.shields.io/pypi/v/package-name?style=for-the-badge"></a>
</div>

<br>

Paragraph describing what the package does here.

## Running the service

Depending on the source and sink you choose to read and write data from, environment variables will need to be set.
The program will inform you of missing env vars, but you can also check the 
[config](src/nwp_consumer/internal/config/config.py) for the given module.

### CLI

Whether running via Docker or the Python package, available commands can be found with the command `help` or the 
`--help` flag. For example:

```shell
$ nwp-consumer --help
# or
$ docker run ghcr.io/openclimatefix/nwp-consumer:latest --help
```

## Ubiquitous Language

The following terms are used throughout the codebase and documentation. They are defined here to avoid ambiguity.

- ***InitTime*** - The time at which a forecast is initialised. For example, a forecast initialised at 12:00 on 1st 
January.

- ***TargetTime*** - The time at which a predicted value is valid. For example, a forecast with InitTime 12:00 on 1st 
January predicts that the temperature at TargetTime 12:00 on 2nd January at position x will be 10 degrees.


## Repository structure

Produced using [exa](https://github.com/ogham/exa):
```shell
$ exa --tree --git-ignore -F -I "*init*|test*.*"
```

```yml
./
├── Containerfile # Dockerfile for building the image
├── pyproject.toml # The build configuration for the service
├── README.md
└── src/
   ├── package_name/ # The python package
   │  ├── cmd/
   │  │  └── main.py # The entrypoint for the service
   │  └── internal/ # Packages internal to the service. Akin to 'lib' folder
   │     ├── config/
   │     │  └── config.py # Configuration for the service
   │     ├── models.py
   │     ├── outputs/ # Holds subpackages for each data sink
   │     └── service/ # Contains the business logic and use-cases of the application

```

`package-name` is structured following principles from the hexagonal architecture pattern. In brief, this means a clear 
separation between the application's business logic - it's **Core** - and the **Actors** that are external to it. In 
this package, the core of the service is in `internal/service/` and the actors are in `internal/inputs/` and 
`internal/outputs/`. The service logic has no knowledge of the external actors, instead defining interfaces that the 
actors must implement. These are found in `internal/models.py`. The actors are then responsible for implementing these 
interfaces, and are *dependency-injected* in at runtime. This allows the service to be easily tested and extended. See
[further reading](#further-reading) for more information.

## Local development

Clone the repository and create and activate a new python virtualenv for it. `cd` to the repository root.

Install the [Python](#python-requirements) dependencies as shown in the section
below.

### Python requirements

Install the required python dependencies (including dev dependencies) and make it editable with

```shell
$ pip install -e .[dev] 
```

This looks for requirements specified in the `pyproject.toml` file.

<details>
    <summary>Where is the requirements.txt file?</summary>

There is no `requirements.txt` file. Instead, the project uses setuptool's pyproject.toml integration to specify 
dependencies. This is a new feature of setuptools and pip, and is the 
[recommended way](https://packaging.python.org/en/latest/tutorials/packaging-projects/) to specify dependencies.
See [the setuptools guide](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) and
[the PEP621 specification](https://packaging.python.org/en/latest/specifications/declaring-project-metadata)
for more information, as well as [Further Reading](#further-reading).
</details>

### Running tests

Ensure you have installed the [Python requirements](#python-requirements).

Run the unit tests with

```shell
$ python -m unittest discover -s src/package_name -p "test_*.py"
```

and the integration tests with

```shell
$ python -m unittest discover -s test_integration -p "test_*.py"
```

See [further reading](#further-reading) for more information on the `src` directory structure.


### Linting and autoformatting

This project uses [Ruff](https://github.com/charliemarsh/ruff) for linting and autoformatting.
It can be run whilst developing via

```shell
$ ruff check --watch --fix src
```


---

## Further reading

On packaging a python project using setuptools and pyproject.toml:
- The official [PyPA packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
- A [step-by-step practical guide](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)
on the *godatadriven* blog.
- The pyproject.toml
[metadata specification](https://packaging.python.org/en/latest/specifications/declaring-project-metadata).

On hexagonal architecture:
- A [concrete example](https://medium.com/towards-data-engineering/a-concrete-example-of-the-hexagonal-architecture-in-python-d821213c6fb9)
using Python.
- An [overview of the fundamentals](https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c) 
incorporating Typescript 
- Another [example](https://medium.com/@matiasvarela/hexagonal-architecture-in-go-cfd4e436faa3) using Go.

On the directory structure:
- The official [PyPA discussion](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) on 
src and flat layouts.

---