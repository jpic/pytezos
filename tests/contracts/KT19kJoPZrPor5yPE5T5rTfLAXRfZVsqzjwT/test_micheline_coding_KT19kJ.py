from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT19kJ(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        code = get_data(
            path='contracts/KT19kJoPZrPor5yPE5T5rTfLAXRfZVsqzjwT/code_KT19kJ.json')
        cls.schema = dict(
            parameter=build_schema(code[0]),
            storage=build_schema(code[1])
        )

    def test_micheline_inverse_storage_KT19kJ(self):
        expected = get_data(
            path='contracts/KT19kJoPZrPor5yPE5T5rTfLAXRfZVsqzjwT/storage_KT19kJ.json')
        decoded = decode_micheline(expected, self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)
