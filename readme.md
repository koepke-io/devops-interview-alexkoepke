# energyhub devops code sample

Hi! Welcome to the EnergyHub DevOps code sample. Your assignment will be to write python code that mimics the type of code you would be writing during your day to day work. You will be writing code that would become the origins of a theoretical build server, which reads from (a mock of) AWS S3.

During the assignment you will be using https://github.com/spulec/moto to mock calls to AWS S3, the resultant code will not network requests and will not require an AWS account.

The goals of the assignment are as follows:

1. Create a readme / setup scripts such that any given engineer can run this code. Ideally in a isolated environment that does not unduly interfere with or modify system packages on their local machine.
2. Fix the core application code in `buildserver.builder` such that the unit tests in `buildtest.test_builder` pass.
3. Add a unit test framework so that you can run the unit tests via CLI
4. Add a linter to ensure good code quality, make the linter run before the unit tests via CLI
5. Add a CLI framework to the core `buildserver.builder` application that can be accessed more or less like so: `builder list-assets`
6. Add a web application framework to the core `buildserver.builder` application that can be accessed more or less like so: `curl localhost:$PORT/buildserver/list-assets`

The goal of this assignment is to create what would be a build server / CLI utility, that would be able to run both locally and in AWS. This assignment is untimed, but in total should not take more than 2 hours.

## Thanks For Working on This!

We aim for this to be a reasonable test of your developement skills, and not be unduly taxing to complete. Please let us know if you have any questions!
