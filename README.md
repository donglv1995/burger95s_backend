# buger95s_backend

This is a template that can be used for new python packages.

## Installation

## Local Development

Run the API with `uvicorn src.burger95s.main:app --reload --port 9999`.

# Development

## Environment
You can read the specific `README.md` from the example you are looking at for details, but the installation procude globally is
* Create you local virtual environment: `python3 -m venv .venv`
* Activate the virtual environment: `.venv/bin/activate` (Linux or WSL), `.venv\Scripts\activate.bat` (cmd.exe), `.venv\Scripts\activate.ps1` (Powershell)
* Upgrade pip and setuptools: `python3 -m pip install pip setuptools --upgrade`
* Install dependencies: `python3 -m pip install -r requirements.txt` (`requirements.txt` is at the root of the repository)
* Install test dependencies: `python3 -m pip install -r requirements-test.txt` (`requirements-test.txt` is at the root of the repository)
* Prepare your environment variables.      

## Swagger Docs
You can read specific API by access url `/docs`

## Linting

## Unit Tests

Local tests can be run using `pytest`
You need to install the test requirements with `pip install -r requirements-test.txt`, then run tests with `pytest tests`.

If you are intersted in covarage, you can run `coverage run -m pytest tests` followed by `coverage report`.
`coverage run` generates a `.coverage` file (excluded from source control) which is read back by `coverage report`.

You can run both the linter and unit tests with `./scripts/runtests.sh` from wsl/linux

## Release