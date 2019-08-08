from unittest import TestCase

from tests import get_data
from pytezos.michelson.coding import micheline_to_michelson, michelson_to_micheline


class MichelsonCodingTestKT1Ce9(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Ce9(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/code_KT1Ce9.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/code_KT1Ce9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Ce9(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/code_KT1Ce9.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/code_KT1Ce9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Ce9(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/code_KT1Ce9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Ce9(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/storage_KT1Ce9.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/storage_KT1Ce9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Ce9(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/storage_KT1Ce9.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/storage_KT1Ce9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Ce9(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/storage_KT1Ce9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooxrXG(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooxrXG.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooxrXG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooxrXG(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooxrXG.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooxrXG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooxrXG(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooxrXG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oopaer(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oopaer.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oopaer.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oopaer(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oopaer.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oopaer.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oopaer(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oopaer.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opEbxt(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opEbxt.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opEbxt.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opEbxt(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opEbxt.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opEbxt.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opEbxt(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opEbxt.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooYaRG(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooYaRG.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooYaRG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooYaRG(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooYaRG.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooYaRG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooYaRG(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooYaRG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ony5uQ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ony5uQ.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ony5uQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ony5uQ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ony5uQ.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ony5uQ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ony5uQ(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ony5uQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooWRdi(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooWRdi.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooWRdi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooWRdi(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooWRdi.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooWRdi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooWRdi(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooWRdi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opZvXV(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opZvXV.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opZvXV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opZvXV(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opZvXV.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opZvXV.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opZvXV(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opZvXV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oovwm5(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oovwm5.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oovwm5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oovwm5(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oovwm5.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oovwm5.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oovwm5(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oovwm5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opM77Y(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opM77Y.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opM77Y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opM77Y(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opM77Y.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opM77Y.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opM77Y(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opM77Y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onm5UE(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_onm5UE.json')
        actual = michelson_to_micheline(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_onm5UE.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onm5UE(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_onm5UE.tz')
        actual = micheline_to_michelson(get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_onm5UE.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onm5UE(self):
        expected = get_data(
            path='/home/mickey/pytezos/tests/contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_onm5UE.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
