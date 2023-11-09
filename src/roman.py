def convert_decimal_to_roman(decimal: int) -> str:
    decimal = abs(decimal)
    if decimal == 0:
        return "N"
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    i = 0
    while decimal > 0:
        for _ in range(decimal // values[i]):
            roman += symbols[i]
            decimal -= values[i]
        i += 1
    return roman


def convert_to_confusing_roman(roman: str) -> str:
    roman = roman.replace("M", "1000")
    roman = roman.replace("D", "500")
    roman = roman.replace("C", "100")
    roman = roman.replace("L", "50")
    roman = roman.replace("X", "10")
    roman = roman.replace("V", "5")
    roman = roman.replace("I", "1")
    return roman


def get_number(number: int, use_roman: bool) -> str:
    if use_roman:
        return convert_decimal_to_roman(number)
    else:
        return str(number)
