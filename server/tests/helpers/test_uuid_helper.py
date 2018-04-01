import re
import unittest
from app.helpers.uuid_helper import generate_uuid

class UUUIDGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        # UUID rules
        # hexDigit =
        #   "0" / "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9" /
        #   "a" / "b" / "c" / "d" / "e" / "f" /
        #   "A" / "B" / "C" / "D" / "E" / "F"
        # UUID -> {8}-{4}-{4}-{4}-{12}
        # regex ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
        self.first_eight_chars = self._generate_reg(8)
        self.second_four_chars = self._generate_reg(4)
        self.third_four_chars = self._generate_reg(4)
        self.fourth_four_chars = self._generate_reg(4)
        self.fifth_twelve_chars = self._generate_reg(12)

        self.reg_pattern = "^%s-%s-%s-%s-%s$" % (self.first_eight_chars,
                                                 self.second_four_chars,
                                                 self.third_four_chars,
                                                 self.fourth_four_chars,
                                                 self.fifth_twelve_chars)
        # re.I stands for IGNORECASE
        # re.M stands for MULTILINE
        # docmentation https://docs.python.org/2/library/re.html#re.compile
        self.regex = re.compile(self.reg_pattern, re.I|re.M)

    def test_uuid_generator_return_valid_uuid(self):
        # arrange
        uuid_value = generate_uuid()

        # act
        valid_uuid = self.regex.match(uuid_value)

        # assert
        self.assertTrue(valid_uuid)

    def _generate_reg(self, length_allowed):
        return "[0-9a-fA-F]{%s}" % length_allowed
