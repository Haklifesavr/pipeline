import unittest
import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to
from apache_beam.transforms import Create
from main import FilterAndSumFn  # import the class from your main script

class FilterAndSumFnTest(unittest.TestCase):
    def test_filter_and_sum_fn(self):
        with TestPipeline() as p:
            input_data = ['2023-06-08,100.0', '2009-01-01,50.0', '2023-06-08,30.0']
            expected_output = [('2023-06-08', 100.0), ('2023-06-08', 30.0)]

            pcoll = p | Create(input_data)
            output = pcoll | 'Filter and map to KV' >> beam.ParDo(FilterAndSumFn())

            assert_that(output, equal_to(expected_output))

    def test_filter_and_sum_fn_fail(self):
        with TestPipeline() as p:
            input_data = ['2023-06-08,100.0', '2009-01-01,50.0', '2023-06-08,30.0']
            expected_output = [('2023-06-08', 100.0), ('2023-06-08', 30.0), ('2009-01-01', 50.0)]

            pcoll = p | Create(input_data)
            output = pcoll | 'Filter and map to KV' >> beam.ParDo(FilterAndSumFn())

            assert_that(output, equal_to(expected_output))

if __name__ == '__main__':
    unittest.main()
