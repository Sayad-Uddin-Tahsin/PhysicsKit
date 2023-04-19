import typing
import physics.exceptions


# Convert units to meters
def cm_to_m(cm: float) -> float:
    """
    Convert centimeters to meters.
    :param cm: The value in centimeters.
    :return: The value converted to meters.
    """
    return cm / 100


def mm_to_m(mm: float) -> float:
    """
    Convert millimeters to meters.
    :param mm: The value in millimeters.
    :return: The value converted to meters.
    """
    return mm / 1000


def km_to_m(km: float) -> float:
    """
    Convert kilometers to meters.
    :param km: The value in kilometers.
    :return: The value converted to meters.
    """
    return km * 1000


def miles_to_m(miles: float) -> float:
    """
    Convert miles to meters.
    :param miles: The value in miles.
    :return: The value converted to meters.
    """
    return miles * 1609.34


def feet_to_m(feet: float) -> float:
    """
    Convert feet to meters.
    :param feet: The value in feet.
    :return: The value converted to meters.
    """
    return feet * 0.3048


def yards_to_m(yards: float) -> float:
    """
    Convert yards to meters.
    :param yards: The value in yards.
    :return: The value converted to meters.
    """
    return yards * 0.9144


def inches_to_m(inches: float) -> float:
    """
    Convert inches to meters.
    :param inches: The value in inches.
    :return: The value converted to meters.
    """
    return inches * 0.0254


# Convert units to kilograms
def g_to_kg(g: float) -> float:
    """
    Convert grams to kilograms.
    :param g: The value in grams.
    :return: The value converted to kilograms.
    """
    return g / 1000


def mg_to_kg(mg: float) -> float:
    """
    Convert milligrams to kilograms.
    :param mg: The value in milligrams.
    :return: The value converted to kilograms.
    """
    return mg / 1000000


def t_to_kg(t: float) -> float:
    """
    Convert metric tons to kilograms.
    :param t: The value in metric tons.
    :return: The value converted to kilograms.
    """
    return t * 1000


def lbs_to_kg(lbs: float) -> float:
    """
    Convert pounds to kilograms.
    :param lbs: The value in pounds.
    :return: The value converted to kilograms.
    """
    return lbs * 0.453592


def oz_to_kg(oz: float) -> float:
    """
    Convert ounces to kilograms.
    :param oz: The value in ounces.
    :return: The value converted to kilograms.
    """
    return oz * 0.0283495


def convert_to_meters(input_string: str) -> typing.Optional[float]:
    """
    Convert any unit to meters.
    :param input_string: A string representing the value and unit
    :return: The value converted to meters, or None if the conversion could not be performed.
    :raises UnitConversionError: if the input string does not contain a valid numeric value or invalid unit given.
    """
    value_str = ''
    unit = ''
    for i, char in enumerate(input_string):
        if char.isdigit() or char == '.':
            value_str += char
        else:
            unit = input_string[i:].strip().lower()
            break
    if not value_str or not unit:
        return None
    try:
        value = float(value_str)
    except ValueError:
        raise physics.exceptions.UnitConversionError("Invalid numeric value in input string")

    if unit == 'm':
        return value
    elif unit == 'cm':
        return cm_to_m(value)
    elif unit == 'mm':
        return mm_to_m(value)
    elif unit == 'km':
        return km_to_m(value)
    elif unit == 'mi':
        return miles_to_m(value)
    elif unit == 'ft':
        return feet_to_m(value)
    elif unit == 'yd':
        return yards_to_m(value)
    elif unit == 'in':
        return inches_to_m(value)
    else:
        raise physics.exceptions.UnitConversionError(f"Invalid unit '{unit}' in input string")


def convert_to_kg(input_string: str) -> typing.Optional[float]:
    """
    Convert any unit of weight to kilograms.
    :param input_string: A string representing the value and unit
    :return: The value converted to kilograms, or None if the conversion could not be performed.
    :raises UnitConversionError: if the input string does not contain a valid numeric value or invalid unit given.
    """
    value_str = ''
    unit = ''
    for i, char in enumerate(input_string):
        if char.isdigit() or char == '.':
            value_str += char
        else:
            unit = input_string[i:].strip().lower()
            break
    if not value_str or not unit:
        return None

    try:
        value = float(value_str)
    except ValueError:
        raise physics.exceptions.UnitConversionError("Invalid numeric value in input string")


    if unit == 'kg':
        return value
    elif unit == 'g':
        return g_to_kg(value)
    elif unit == 'mg':
        return mg_to_kg(value)
    elif unit == 't':
        return t_to_kg(value)
    elif unit == 'lbs':
        return lbs_to_kg(value)
    elif unit == 'oz':
        return oz_to_kg(value)
    else:
        raise physics.exceptions.UnitConversionError(f"Invalid unit '{unit}' in input string")
