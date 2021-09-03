# py-fhe
A Python 3 library for fully homomorphic encryption. Currently, this library includes an implementation of the Brakerski-Fan-Vercauteren (BFV) scheme, the Cheon-Kim-Kim-Song (CKKS) scheme, and bootstrapping for CKKS.

## Installation and Run
* #### Linux

    ```sh
    # To install the library run the following command in the root folder:
    pip install -e .

    # Run the example.py for bfv and ckks
    cd examples

    python3 ckks_mult_examples.py
    ```

This should install the necessary dependencies.

## Tests
    
    ```sh
    # You can run all the unit tests as follows:
    
    pytest

    #To run a specific test file (i.e. test_polynomial.py), you can run the file using Python 3 with the command

    python3 tests/test_polynomial.py

    #To run all tests in a single class from a test file (i.e. TestPolynomial from tests/test_polynomial.py), you can use the command

    python3 tests/test_polynomial.py TestPolynomial

    #To run a specific test from a test file (i.e. TestPolynomial.test_add from tests/test_polynomial.py), you can use the command

    python3 tests/test_polynomial.py TestPolynomial.test_add
    ```

## Examples
See the examples folder for examples on how to use the library.
