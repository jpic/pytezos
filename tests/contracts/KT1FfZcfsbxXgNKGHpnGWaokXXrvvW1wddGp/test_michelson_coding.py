from unittest import TestCase

from tests import get_data
from pytezos.michelson.coding import micheline_to_michelson, michelson_to_micheline


class MichelsonCodingTestKT1FfZ(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1FfZ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/code_KT1FfZ.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/code_KT1FfZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1FfZ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/code_KT1FfZ.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/code_KT1FfZ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1FfZ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/code_KT1FfZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1FfZ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/storage_KT1FfZ.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/storage_KT1FfZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1FfZ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/storage_KT1FfZ.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/storage_KT1FfZ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1FfZ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/storage_KT1FfZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onz3sp(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onz3sp.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onz3sp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onz3sp(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onz3sp.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onz3sp.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onz3sp(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onz3sp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op3k3r(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_op3k3r.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_op3k3r.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op3k3r(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_op3k3r.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_op3k3r.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op3k3r(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_op3k3r.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooWtpV(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooWtpV.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooWtpV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooWtpV(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooWtpV.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooWtpV.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooWtpV(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooWtpV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onhoAS(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onhoAS.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onhoAS.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onhoAS(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onhoAS.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onhoAS.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onhoAS(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_onhoAS.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooZzzH(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooZzzH.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooZzzH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooZzzH(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooZzzH.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooZzzH.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooZzzH(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooZzzH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo9vEm(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo9vEm.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo9vEm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo9vEm(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo9vEm.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo9vEm.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo9vEm(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo9vEm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opKR3R(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opKR3R.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opKR3R.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opKR3R(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opKR3R.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opKR3R.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opKR3R(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opKR3R.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo1VyF(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo1VyF.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo1VyF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo1VyF(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo1VyF.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo1VyF.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo1VyF(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_oo1VyF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooJN2s(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooJN2s.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooJN2s.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooJN2s(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooJN2s.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooJN2s.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooJN2s(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_ooJN2s.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opUxWC(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opUxWC.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opUxWC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opUxWC(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opUxWC.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opUxWC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opUxWC(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1FfZcfsbxXgNKGHpnGWaokXXrvvW1wddGp/parameter_opUxWC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
