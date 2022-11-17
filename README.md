# EnergyHub DevOps Code Sample

Hi! Welcome to the EnergyHub DevOps code sample.

This repository contains a simple Python web app called `buildserver`. Your goal will be to add a status-check endpoint to this app, and then implement a CI process that will package the app into a container image and publish it to our container registry.

This assignment is untimed, but in total should not take more than two hours.

## The assignment

Specifically, the goals of your assignment are as follows:

1. Add a new endpoint `/status` to the `buildserver` app, which should return a JSON object as follows:

    ```json
    {
      "pid": 1234,
      "status": "OK"
    }
    ```

    where `1234` is the current process ID of the application.
2. Add appropriate unit tests for the new endpoint.
3. Add a mechanism for packaging the app as a container image.
4. Add a CI workflow using GitHub Actions that will build the image on each commit and push the image to the GitHub Container Registry. The image should be tagged with the commit SHA.
5. Add a "Release process" section to this README describing how and when images are built and any other steps an engineer would need to perform in order to release a new version of the app. (If you come across any other documentation gaps, feel free to add additional info.)

## Submission

Please push your changes to a branch in this repository (no need to fork the repo) and open a GitHub pull request against `main`. We will be reviewing your pull request on the following criteria:

- Good development practices
- Clarity in code and documentation
- Correctness and completeness of your solution

## Thanks!

We hope this is fun. Please let us know if you have any questions, and good luck!
