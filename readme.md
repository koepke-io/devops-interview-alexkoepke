# EnergyHub DevOps Code Sample

Hi! Welcome to the EnergyHub DevOps code sample. Your assignment will be to write python code that mimics the type of code you would be writing during your day to day work. You will be writing code that would become the origins of a theoretical build server, which reads from (a mock of) AWS S3.

During the assignment you will be using https://github.com/spulec/moto to mock calls to AWS S3, the resultant code will not make network requests and will not require an AWS account.

## The Assignment

The goals of the assignment are as follows:

1. Create a readme / setup scripts such that any given engineer can run this code. Ideally in a isolated environment that does not unduly interfere with or modify system packages on their local machine.
2. Add a unit test framework so that you can run the unit tests, and instructions for running the unit tests via CLI
3. Add a linter to ensure good code quality, and instructions for running the linter via CLI
4. Fix the core application code in `buildserver.builder` such that the unit tests in `buildtest.test_builder` pass.
5. Add a `put_asset` function to builder, and an associated unit test
6. Add a CLI framework to the core `buildserver.builder` application that can be accessed more or less like so: `builder put-asset`
7. Add a web application framework to the core `buildserver.builder` application that can be accessed more or less like so: `curl localhost:$PORT/buildserver/put-asset`
8. Add documentation on usage of the unit tests, linters, CLI, and web server

The goal of this assignment is to create what would be a build server / CLI utility, that would be able to run both locally via CLI and as a web server in AWS. This assignment is untimed, but in total should not take more than 2 hours.

## Grading

We will be primarily evaluating your assignment based on the following criteria:

- Effectiveness of setup scripts
- Correctness and completeness of assignment
- Clarity in code and documentation

As DevOps engineers we often are tasked with producing low complexity code, but high quality documentation, and that is the goal you should strive for with your assignment. Feel encouraged to show off your strongest skills!

## Thanks For Working on This!

We aim for this to be a reasonable test of your development skills, and not be unduly taxing to complete. It should be vaguely similar prior work you have done in your career, assuming you have spent time doing some light scripting in python or some similar language. Please let us know if you have any questions, and good luck with the assignment!
