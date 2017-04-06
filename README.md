Installation

Install mongodb

example:
        apt install mongodb


Clone the repo and install and create a new environmet using virtualenv:

virtualenv ENV

source ENV/bin/activate

Once you have created and activated the environment you have to install the dependencies:

make init 

Tests

All the tests are into tests directory. You can run them using:

make test

If you want to know the coverage, first run "mongod" and you can use:

make coverage