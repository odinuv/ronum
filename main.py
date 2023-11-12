import streamlit as st

from src.calc import calculate, validate
from src.roman import get_number, convert_to_confusing_roman, convert_decimal_to_roman


def number_clicked(number: int) -> None:
    if st.session_state.enter_clicked:
        st.session_state.next_number = '0'
        st.session_state.enter_clicked = False

    st.session_state.next_number = str(st.session_state.next_number) + str(number)
    st.session_state.result_text = int(st.session_state.next_number)


def operation_clicked(operation: str) -> None:
    st.session_state.enter_clicked = True
    if st.session_state.next_operation is None:
        st.session_state.result = int(st.session_state.next_number)
        st.session_state.next_operation = operation
        return

    st.session_state.result = calculate(
        st.session_state.next_operation,
        st.session_state.result,
        int(st.session_state.next_number)
    )

    st.session_state.next_operation = operation
    st.session_state.result_text = int(st.session_state.result)


def enter_clicked() -> None:
    st.session_state.enter_clicked = True
    if st.session_state.next_operation is None:
        st.session_state.result = int(st.session_state.next_number)

    if st.session_state.next_operation is None:
        return

    st.session_state.result = calculate(
        st.session_state.next_operation,
        st.session_state.result,
        int(st.session_state.next_number)
    )

    st.session_state.result_text = int(st.session_state.result)


def clear() -> None:
    st.session_state.next_operation = None
    st.session_state.next_number = '0'
    st.session_state.result_text = '0'
    st.session_state.result = 0


def clear_clicked() -> None:
    clear()


def dot_clicked(info_container) -> None:
    info_container.info('FYI the Roman Numeral system included [fractions]('
                        'https://en.wikipedia.org/wiki/Roman_numerals#Fractions). Though not decimal, '
                        'but [duodecimal](https://en.wikipedia.org/wiki/Duodecimal).')


def numlock_clicked(video_container) -> None:
    video_container.markdown(
        '''<iframe width='462' height='822'
        src='https://www.youtube.com/embed/1bvtlQJ17qo?autoplay=1'
        title='A fight between NumLock &amp; ScrollLock' frameborder='0'
        allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share'
        allowfullscreen>
        </iframe>''',
        unsafe_allow_html=True)


def init_session() -> None:
    if 'result' not in st.session_state:
        st.session_state['result'] = 0
    if 'result_text' not in st.session_state:
        st.session_state['result_text'] = '0'
    if 'next_operation' not in st.session_state:
        st.session_state['next_operation'] = None
    if 'next_number' not in st.session_state:
        st.session_state['next_number'] = '0'
    if 'enter_clicked' not in st.session_state:
        st.session_state['enter_clicked'] = False
    # logger = get_logger(__name__)
    # logger.info(st.session_state.result)
    # logger.info(st.session_state.result_text)
    # logger.info(st.session_state.next_operation)
    # logger.info(st.session_state.next_number)
    # logger.info(st.session_state.enter_clicked)


def run() -> None:
    init_session()

    st.set_page_config(
        page_title='Confusing calculator',
        page_icon=':abacus:',
    )

    css_style = '''
    /* calc layout */
    div[data-testid='stVerticalBlock'] {
        width: 370px;
        margin: auto;
    }
    div[data-testid='stVerticalBlock'] div[data-testid='stVerticalBlock'] {
        width: auto;
    }
    div[data-testid='stHorizontalBlock'] {
        width: 370px;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='element-container'] {
        margin: auto;
        width: fit-content !important;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='element-container'] {
        margin: auto;
        width: fit-content !important;
    }

    /* All buttons */
    div[data-testid='stHorizontalBlock'] div[data-testid='element-container']
    button[data-testid='baseButton-secondary'] {
        background-color: #00a6ed;
        width: 80px;
        height: 80px;
        display: block;
        margin: auto;
        color: #000000;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='element-container']
    button[data-testid='baseButton-secondary'] p {
        font-size: 32px;
    }

    /* Plus button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(4)
    div[data-testid='element-container']:nth-child(2) button {
        height: 176px;
        background-color: #00d26a;
    }

    /* Enter button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(4)
    div[data-testid='element-container']:nth-child(3) button {
        background-color: #fcd53f;
        height: 176px;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(4)
    div[data-testid='element-container']:nth-child(3) button p {
        font-size: 18px;
    }

    /* Zero button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(1)
    div[data-testid='element-container']:nth-child(5) button {
        width: 176px;
    }

    /* Numlock button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(1)
    div[data-testid='element-container']:nth-child(1) button p {
        font-size: 18px;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(1)
    div[data-testid='element-container']:nth-child(1) button {
        background-color: #fcd53f;
    }

    /* Division button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(2)
    div[data-testid='element-container']:nth-child(1) button p {
        font-size: 18px;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(2)
    div[data-testid='element-container']:nth-child(1) button {
        background-color: #00d26a;
    }

    /* Multiplication button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(3)
    div[data-testid='element-container']:nth-child(1) button p {
        font-size: 18px;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(3)
    div[data-testid='element-container']:nth-child(1) button {
        background-color: #00d26a;
    }

    /* Minus button */
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(4)
    div[data-testid='element-container']:nth-child(1) button p {
        font-size: 18px;
    }
    div[data-testid='stHorizontalBlock'] div[data-testid='column']:nth-child(4)
    div[data-testid='element-container']:nth-child(1) button {
        background-color: #00d26a;
    }

    /* Clear button */
    div[data-testid='stHorizontalBlock']:nth-child(3) div[data-testid='column']:nth-child(2)
    div[data-testid='element-container']:nth-child(1) button {
        height: 40px;
        margin-left: 98px;
        background-color: #fcd53f;
    }
    div[data-testid='stHorizontalBlock']:nth-child(3) div[data-testid='column']:nth-child(2)
    div[data-testid='element-container']:nth-child(1) button p {
        font-size: 18px;
    }

    /* Result line */
    div[data-testid='stVerticalBlock'] div[data-testid='stVerticalBlock'] div.stMarkdown
    div[data-testid='stMarkdownContainer'] {
        width: 280px !important;
        overflow-x: auto;
    }
    div[data-testid='stVerticalBlock'] div[data-testid='stVerticalBlock'] div.stMarkdown
    div[data-testid='stMarkdownContainer'] p {
        word-break: normal;
        padding-left: 10px;
        padding-right: 10px;
        font-size: 20px;
        background-color: #333333;
    }

    div.stAlert {
        width: 400px;
    }
    '''
    st.markdown(f'<style>{css_style}</style>', unsafe_allow_html=True)
    video_container = st.container()

    st.title('A confusing calculator :abacus:')

    if validate(st.session_state.result) == 2 or validate(int(st.session_state.next_number)) == 2:
        st.error('Bad boy')
        st.image('static/bad_romans.jpg', width=400)
        clear()
    elif validate(st.session_state.result) == 1 or validate(int(st.session_state.next_number)) == 1:
        st.warning('The Romans did not have a number for this.')

    container = st.container()
    with container:
        use_roman = st.toggle('Use Roman keyboard', value=False)
        use_confuser = not st.toggle('Stop modernizing', value=False)

        head_col1, head_col2 = st.columns(2)

        result = str(st.session_state.result_text)
        if use_roman:
            result = convert_decimal_to_roman(int(st.session_state.result_text))
        if use_confuser:
            result = convert_to_confusing_roman(convert_decimal_to_roman(int(st.session_state.result_text)))
        head_col1.write(result)
        head_col2.button('Clear', on_click=clear_clicked)

        col1, col2, col3, col4 = st.columns(4)

        col1.button('Num Lock', on_click=numlock_clicked, args=[video_container])
        col1.button(get_number(7, use_roman), on_click=number_clicked, args=[7])
        col1.button(get_number(4, use_roman), on_click=number_clicked, args=[4])
        col1.button(get_number(1, use_roman), on_click=number_clicked, args=[1])
        col1.button(get_number(0, use_roman), on_click=number_clicked, args=[0])

        col2.button('/', on_click=operation_clicked, args=['/'])
        col2.button(get_number(8, use_roman), on_click=number_clicked, args=[8])
        col2.button(get_number(5, use_roman), on_click=number_clicked, args=[5])
        col2.button(get_number(2, use_roman), on_click=number_clicked, args=[2])

        col3.button('\\*', on_click=operation_clicked, args=['*'])
        col3.button(get_number(9, use_roman), on_click=number_clicked, args=[9])
        col3.button(get_number(6, use_roman), on_click=number_clicked, args=[6])
        col3.button(get_number(3, use_roman), on_click=number_clicked, args=[3])
        col3.button('.', on_click=dot_clicked, args=[container])

        col4.button('\\-', on_click=operation_clicked, args=['-'])
        col4.button('\\+', on_click=operation_clicked, args=['+',])
        col4.button('Enter', on_click=enter_clicked)

    st.markdown('<hr style="width:400px">', unsafe_allow_html=True)
    st.markdown(
        '''

        ### What the heck is this?
        It's a calculator that follows the rule from the xkcd comic.

        ![xkcd - Roman Numerals](/app/static/roman_numerals.png)

        Yeah, so number eight is 5111.

        [Good luck (on your way home)](https://en.wikipedia.org/wiki/Romani_ite_domum)
        '''
    )
    st.image('static/romanus.jpg', width=268)
    st.markdown(
        '''

        Idea by [xkcd](https://xkcd.com/2637/).
        Developed by [Odin](http://odinuv.com/).

        '''
    )


if __name__ == '__main__':
    run()
