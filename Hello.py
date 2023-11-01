# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Confusing calculator",
        page_icon=":abacus:",
    )

    if 'result' not in st.session_state:
        st.session_state['result'] = 0
    if 'result_text' not in st.session_state:
        st.session_state['result_text'] = 'N'
    if 'next_operation' not in st.session_state:
        st.session_state['next_operation'] = None
    if 'next_number' not in st.session_state:
        st.session_state['next_number'] = ''
    if 'enter_clicked' not in st.session_state:
        st.session_state['enter_clicked'] = False

    LOGGER.info(st.session_state.result)
    LOGGER.info(st.session_state.result_text)
    LOGGER.info(st.session_state.next_operation)

    st.markdown("""
                <style>
                    div[data-testid="stVerticalBlock"] {
                        /* background-color: white; */ 
                        width: 370px;
                        margin: auto;
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
                        /* background-color: white; */ 
                        width: auto;
                    }
                    div[data-testid="stHorizontalBlock"] {
                        /* background-color: white; */ 
                        width: 370px;
                    }
                    div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] {
                        margin: auto;                    
                        width: fit-content !important;
                    }
                    div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] {
                        margin: auto;                    
                        width: fit-content !important;
                    }
                    
                    /* All buttons */
                    div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] button[data-testid="baseButton-secondary"] {
                        background-color: green;
                        width: 80px;
                        height: 80px;
                        display: block;
                        margin: auto;
                    }
                    div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] button[data-testid="baseButton-secondary"] p {
                        font-size: 32px;
                    }
                                        
                    /* Plus button */ 
                    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) div[data-testid="element-container"]:nth-child(2) button {
                        height: 176px;
                    }
                    
                    /* Enter button */ 
                    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) div[data-testid="element-container"]:nth-child(3) button {
                        background-color: blue;
                        height: 176px;
                    }
                    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) div[data-testid="element-container"]:nth-child(3) button p {
                        font-size: 18px;
                    }

                    /* Zero button */
                    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) div[data-testid="element-container"]:nth-child(5) button {
                        background-color: red;
                        width: 176px;
                    }
                    
                    /* Numlock button */
                    div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) div[data-testid="element-container"]:nth-child(1) button p {
                        font-size: 18px;
                    }
    
                    /* Clear button */
                    div[data-testid="stHorizontalBlock"]:nth-child(2) div[data-testid="column"]:nth-child(2) div[data-testid="element-container"]:nth-child(1) button {
                        height: 40px;
                        margin-left: 98px;
                    }                     
                    div[data-testid="stHorizontalBlock"]:nth-child(2) div[data-testid="column"]:nth-child(2) div[data-testid="element-container"]:nth-child(1) button p {
                        font-size: 18px;
                    }
                    
                    /* Result line */
                    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div.stMarkdown div[data-testid="stMarkdownContainer"] {
                        width: 280px !important;
                        overflow-x: auto;
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div.stMarkdown div[data-testid="stMarkdownContainer"] p {
                        word-break: normal;
                        font-size: 20px;
                        background-color: #333333;
                    }

                </style>
                """,
                unsafe_allow_html=True)

    def number_clicked(number):
        if st.session_state.enter_clicked:
            st.session_state.next_number = ''
            st.session_state.enter_clicked = False

        st.session_state.next_number = str(st.session_state.next_number) + str(number)

        if (int(st.session_state.next_number) > 4000) or (int(st.session_state.next_number) < 0):
            st.warning('number out of range')
        if (int(st.session_state.next_number) > 40000) or (int(st.session_state.next_number) < -1000):
            st.error('bad boy')
            st.session_state.next_number = ''


        # if st.session_state.next_operation is None:
        #    st.session_state.next_number = str(st.session_state.next_number) + str(number)

        #elif st.session_state.next_operation == '+':
        #    st.session_state.result = st.session_state.result + number
        #elif st.session_state.next_operation == '-':
        #    st.session_state.result = st.session_state.result - number
        #elif st.session_state.next_operation == '*':
        #    st.session_state.result = st.session_state.result * number
        #elif st.session_state.next_operation == '/':
        #    st.session_state.result = st.session_state.result / number
        # result_text = convert_decimal_to_roman(st.session_state.result)
        # st.session_state.result_text = convert_to_confusing_roman(result_text)
        st.session_state.result_text = st.session_state.next_number
        st.session_state.result_text = convert_to_confusing_roman(convert_decimal_to_roman(st.session_state.result_text))

    def operation_clicked(operation):
        st.session_state.enter_clicked = True
        if st.session_state.next_number == '':
            st.session_state.next_operation = operation
            return
        if st.session_state.next_operation is None:
            st.session_state.result = int(st.session_state.next_number)
        elif st.session_state.next_operation == '+':
            st.session_state.result = st.session_state.result + int(st.session_state.next_number)
        elif st.session_state.next_operation == '-':
            st.session_state.result = st.session_state.result - int(st.session_state.next_number)
        elif st.session_state.next_operation == '*':
            st.session_state.result = st.session_state.result * int(st.session_state.next_number)
        elif st.session_state.next_operation == '/':
            st.session_state.result = st.session_state.result / int(st.session_state.next_number)

        if (st.session_state.result > 4000) or (st.session_state.result < 0):
            st.warning('The Romans did not have a number for this.')
        if (st.session_state.result > 40000) or (st.session_state.result < -1000):
            st.error('Bad boy')
            st.session_state.result = 0


        st.session_state.next_operation = operation
        st.session_state.result_text = str(st.session_state.result)
        st.session_state.result_text = convert_to_confusing_roman(convert_decimal_to_roman(st.session_state.result_text))

    def enter_clicked():
        st.session_state.enter_clicked = True
        if st.session_state.next_number == '':
            return
        if st.session_state.next_operation is None:
            st.session_state.result = int(st.session_state.next_number)
        elif st.session_state.next_operation == '+':
            st.session_state.result = st.session_state.result + int(st.session_state.next_number)
        elif st.session_state.next_operation == '-':
            st.session_state.result = st.session_state.result - int(st.session_state.next_number)
        elif st.session_state.next_operation == '*':
            st.session_state.result = st.session_state.result * int(st.session_state.next_number)
        elif st.session_state.next_operation == '/':
            st.session_state.result = st.session_state.result / int(st.session_state.next_number)
        st.session_state.result_text = str(st.session_state.result)
        st.session_state.result_text = convert_to_confusing_roman(convert_decimal_to_roman(st.session_state.result_text))

    def clear_clicked():
        st.session_state.next_operation = None
        st.session_state.next_number = ''
        st.session_state.result_text = 'N'

    def convert_decimal_to_roman(decimal):
        if decimal == '':
            return 'N'
        decimal = int(decimal)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        i = 0
        while decimal > 0:
            for _ in range(decimal // values[i]):
                roman += symbols[i]
                decimal -= values[i]
            i += 1
        if roman == '':
            roman = 'N'
        return roman

    def convert_to_confusing_roman(roman):
        LOGGER.info('confusing')
        LOGGER.info(roman)
        roman = roman.replace('M', '1000')
        LOGGER.info(roman)
        roman = roman.replace('D', '500')
        LOGGER.info(roman)
        roman = roman.replace('C', '100')
        LOGGER.info(roman)
        roman = roman.replace('L', '50')
        LOGGER.info(roman)
        roman = roman.replace('X', '10')
        LOGGER.info(roman)
        roman = roman.replace('V', '5')
        LOGGER.info(roman)
        roman = roman.replace('I', '1')
        LOGGER.info(roman)
        LOGGER.info('done')
        return roman

    def get_number(number, use_roman):
        if use_roman:
            return convert_decimal_to_roman(number)
        else:
            return str(number)

    def dot_clicked(container):
        container.info('FYI the Roman Numeral system included [fractions](https://en.wikipedia.org/wiki/Roman_numerals#Fractions). Though not decimal, but [duodecimal](https://en.wikipedia.org/wiki/Duodecimal).')

    st.title('A confusing calculator :abacus:')

    container = st.container()
    with container:
        use_roman = st.toggle('Use Roman keyboard', value=False)
        hcol1, hcol2 = st.columns(2)
        hcol1.write(st.session_state.result_text)
        hcol2.button('Clear', on_click=clear_clicked)

        col1, col2, col3, col4 = st.columns(4)
        col1.button('Num Lock')
        col1.button(get_number(7, use_roman), on_click=number_clicked, args=[7])
        col1.button(get_number(4, use_roman), on_click=number_clicked, args=[4])
        col1.button(get_number(1, use_roman), on_click=number_clicked, args=[1])
        col1.button(get_number(0, use_roman), on_click=number_clicked, args=[0])

        col2.button('/', on_click=operation_clicked, args=['/'])
        col2.button(get_number(8, use_roman), on_click=number_clicked, args=[8])
        col2.button(get_number(5, use_roman), on_click=number_clicked, args=[5])
        col2.button(get_number(2, use_roman), on_click=number_clicked, args=[2])

        col3.button('\*', on_click=operation_clicked, args=['*'])
        col3.button(get_number(9, use_roman), on_click=number_clicked, args=[9])
        col3.button(get_number(6, use_roman), on_click=number_clicked, args=[6])
        col3.button(get_number(3, use_roman), on_click=number_clicked, args=[3])
        col3.button('.', on_click=dot_clicked, args=[container])

        col4.button('\-', on_click=operation_clicked, args=['-'])
        col4.button('\+', on_click=operation_clicked, args=['+'])
        col4.button('Enter', on_click=enter_clicked)

    st.markdown(
        """
        ### What the heck is this?
        It's a calculator that follows the rule outlined in the following xkcd comic. 
        
        Yeah, so number eight is 5111. 
        
        Good luck.
        
        ![xkcd - Roman Numerals](https://imgs.xkcd.com/comics/roman_numerals.png) 
        
        ![Romanus eunt domus]()
        https://en.wikipedia.org/wiki/Romani_ite_domum
        
        Idea by [xkcd](https://xkcd.com/2637/).
        Developed by [Odin](http://odinuv.com/).
            https://www.kapwing.com/6541e97954a77bfa0f6452fb/studio/editor
        """
    )


if __name__ == "__main__":
    run()
