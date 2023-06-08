import unittest
import apache_beam as beam
import json
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to
from apache_beam.transforms.core import Create

from main import ProcessTransactions


class TransactionsTest(unittest.TestCase):

    def test_process_transactions_pass(self):
        with TestPipeline() as p:
            test_data = [
                '2011-01-01,wallet00000e719adfeaa64b5a,wallet00001866cb7e0f09a890,1021101.99'
            ]
            expected_output = [
                '{"date": "2011-01-01", "sum": 1021101.99}'
            ]

            result = (p 
                    | 'Create Test Data' >> Create(test_data)
                    | 'Process Transactions' >> ProcessTransactions())

            assert_that(result, equal_to(expected_output))
            print("Test passed!")


    def test_process_transactions_fail(self):
        with TestPipeline() as p:
            test_data = [
                '2011-01-01,wallet00000e719adfeaa64b5a,wallet00001866cb7e0f09a890,1021101.99'
            ]
            expected_output = [
                '{"date": "2011-01-01", "sum": 1000000.0}'
            ]

            result = (p 
                      | 'Create Test Data' >> Create(test_data)
                      | 'Process Transactions' >> ProcessTransactions()
                      | 'Map To String' >> beam.Map(json.dumps))

            assert_that(result, equal_to(expected_output))

if __name__ == '__main__':
    unittest.main()
