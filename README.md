# EnergyHub DevOps Code Sample

Hi! Welcome to the EnergyHub DevOps code sample.

This repository contains a simple Python web app called `buildserver`. Your goal will be to add a status-check endpoint to this app, and then implement a CI process that will package the app into a container image and publish it to our container registry.

This assignment is untimed, but in total should not take more than two hours.

## Pre-requisites

Inorder to run this application, you will need to have the following installed on your machine:

- (optional) [pyenv](https://github.com/pyenv/pyenv)
- Python 3.9 or higher
- Docker

## Initial Setup

1. Clone this repository
2. Create a virtual environment and update the build tools:

    ```bash
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip wheel setuptools pip-tools
    ```
3. With the virtual environment activated, install the application dependencies:

    ```bash
    $ make install
    ```
4. Copy the .env.example file to .env and update the values as needed:

    ```bash
    $ cp .env.example .env
    ```

## Running the application
1. Activate the virtual environment:

    ```bash
    $ source venv/bin/activate
    ```
2. Run the application:

    ```bash
    $ make run
    ```
3. Bonus: Testing the docker build

    ```bash
    $ make docker-build
    ```
4. Bonus: Running the docker image

    ```bash
    $ make docker-run
    ```
## Release process

When you are ready to release a new version of the application, you will need to do the following:
1. Update the version number in `pyproject.toml`
2. Run `make all` this will format the code, run the tests, and build then run the docker image in order to verify that everything is working as expected.
3. Open a pull request with your changes and wait for the CI to pass.
4. Once the CI has passed and your changes have been approved, merge the pull request into `main`.



## The assignment

Specifically, the goals of your assignment are as follows:

- [x] Add a new endpoint `/status` to the `buildserver` app, which should return a JSON object as follows:

    ```json
    {
      "pid": 1234,
      "status": "OK"
    }
    ```

    where `1234` is the current process ID of the application.
- [x] Add appropriate unit tests for the new endpoint.
- [x] Add a mechanism for packaging the app as a container image.
- [x] Add a CI workflow using GitHub Actions that will build the image on each commit and push the image to the GitHub Container Registry. The image should be tagged with the commit SHA.
- [x] Add a "Release process" section to this README describing how and when images are built and any other steps an engineer would need to perform in order to release a new version of the app. (If you come across any other documentation gaps, feel free to add additional info.)

## Submission

Please push your changes to a branch in this repository (no need to fork the repo) and open a GitHub pull request against `main`. We will be reviewing your pull request on the following criteria:

- Good development practices
- Clarity in code and documentation
- Correctness and completeness of your solution

## Thanks!

We hope this is fun. Please let us know if you have any questions, and good luck!
