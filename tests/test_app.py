import unittest
from streamlit.testing.v1 import AppTest
import os

from streamlit.testing.v1.element_tree import Button


class TestApp(unittest.TestCase):
    @staticmethod
    def cwd_root_directory() -> None:
        current_file_path = os.path.realpath(__file__)
        current_directory = os.path.dirname(current_file_path)
        os.chdir(current_directory + '/../')

    def test_run_calc(self) -> None:
        self.cwd_root_directory()

        at = AppTest.from_file('main.py')
        at.run()
        self.assertEqual('A confusing calculator :abacus:', at.title[0].value)

        button_9 = self.find_button(at, '9')
        button_9.click()
        at.run()
        self.assertEqual('110', at.markdown[1].value)

        button_8 = self.find_button(at, '8')
        button_8.click()
        at.run()
        self.assertEqual('101005111', at.markdown[1].value)

        button_clear = self.find_button(at, 'Clear')
        button_clear.click()
        at.run()
        self.assertEqual('N', at.markdown[1].value)

        button_7 = self.find_button(at, '7')
        button_7.click()
        at.run()
        self.assertEqual('511', at.markdown[1].value)

        button_plus = self.find_button(at, '\\+')
        button_plus.click()
        at.run()
        self.assertEqual('511', at.markdown[1].value)

        button_6 = self.find_button(at, '6')
        button_6.click()
        at.run()
        self.assertEqual('51', at.markdown[1].value)

        button_plus = self.find_button(at, '\\+')
        button_plus.click()
        at.run()
        self.assertEqual('10111', at.markdown[1].value)

        button_enter = self.find_button(at, 'Enter')
        button_enter.click()
        at.run()
        self.assertEqual('10110', at.markdown[1].value)

    def test_run_warnings(self) -> None:
        self.cwd_root_directory()

        at = AppTest.from_file('main.py')
        at.run()

        button_5 = self.find_button(at, '5')
        button_5.click()
        at.run()

        button_4 = self.find_button(at, '4')
        button_4.click()
        at.run()

        button_3 = self.find_button(at, '3')
        button_3.click()
        at.run()

        button_2 = self.find_button(at, '2')
        button_2.click()
        at.run()
        self.assertEqual('The Romans did not have a number for this.', at.warning[0].value)
        self.assertEqual('1000100010001000100010050010101011', at.markdown[1].value)

        button_1 = self.find_button(at, '1')
        button_1.click()
        at.run()

        self.assertEqual('N', at.markdown[1].value)
        self.assertEqual('Bad boy, you ignored the warning', at.error[0].value)

    def test_toggle_key_pad_only(self) -> None:
        self.cwd_root_directory()

        at = AppTest.from_file('main.py')
        at.run()

        roman_numeral = at.toggle[0]
        roman_numeral.set_value(True)

        confuse_off = at.toggle[1]
        confuse_off.set_value(False)

        at.run()
        button_4 = self.find_button(at, 'IV')
        button_4.click()
        at.run()
        self.assertEqual('15', at.markdown[1].value)

    def test_toggle_key_pad_and_result(self) -> None:
        self.cwd_root_directory()

        at = AppTest.from_file('main.py')
        at.run()

        roman_numeral = at.toggle[0]
        roman_numeral.set_value(True)

        confuse_off = at.toggle[1]
        confuse_off.set_value(True)

        at.run()
        button_4 = self.find_button(at, 'IV')
        button_4.click()
        at.run()
        self.assertEqual('IV', at.markdown[1].value)

    def test_toggle_to_decimal(self) -> None:
        self.cwd_root_directory()

        at = AppTest.from_file('main.py')
        at.run()

        roman_numeral = at.toggle[0]
        roman_numeral.set_value(False)

        confuse_off = at.toggle[1]
        confuse_off.set_value(True)

        at.run()
        button_4 = self.find_button(at, '4')
        button_4.click()
        at.run()
        self.assertEqual('4', at.markdown[1].value)

        # Does not work https://github.com/streamlit/streamlit/issues/7711
        # button_dot = self.find_button(at, '.')
        # button_dot.click()
        # at.run()
        # self.assertEqual(at.info[0].label, 'Invalid input')

        # button_num_lock = self.find_button(at, 'Num Lock')
        # button_num_lock.click()
        # at.run()
        # self.assertEqual(at.info[0].label, 'Invalid input')

    @staticmethod
    def find_button(at: AppTest, label: str) -> Button:
        for i in range(at.button.len):
            if at.button[i].label == label:
                return at.button[i]
