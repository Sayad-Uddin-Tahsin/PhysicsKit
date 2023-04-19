import typing
from . import constants

G = 6.67430e-11


def Gforce(m1: float, m2: float, d: float, G: typing.Optional[float] = G) -> float:
    """
    Calculate the gravitational force between two objects.

    :param m1: The mass of the first object in kilograms.
    :param m2: The mass of the second object in kilograms.
    :param d: The distance between the two objects in meters.
    :param G: The Gravitational Constant, defaults to 6.67430×10⁻¹¹.
    :return: The gravitational force between the two objects in Newtons.
    """
    Gforce = G * ((m1 * m2) / (d ** 2))
    return Gforce


def distance(m1: float, m2: float, F: float, G: typing.Optional[float] = G) -> float:
    """
    Calculate the distance between two objects.

    :param m1: The mass of the first object in kilograms.
    :param m2: The mass of the second object in kilograms.
    :param F: The gravitational force between m₁ and m₂.
    :param G: The Gravitational Constant, defaults to 6.67430×10⁻¹¹.
    :return: The distance between m₁ and m₂ in Meters.
    """
    distance = ((G * m1 * m2) / F) ** (1 / 2)
    return distance


def gravitational_constant(m1: float, m2: float, d: float, F: float) -> float:
    """
    Calculate the Gravitational Constant.

    :param m1: The mass of the first object in kilograms.
    :param m2: The mass of the second object in kilograms.
    :param d: The distance between m₁ and m₂.
    :param F: The gravitational force between m₁ and m₂.
    :return: The Gravitational Constant
    """
    gConstant = F * d ** 2 / (m1 * m2)
    return gConstant


def m1(m2: float, d: float, F: float, G: typing.Optional[float] = G) -> float:
    """
    Calculate the mass of the first object.

    :param m2: The mass of the second object in kilograms.
    :param d: The distance between m₁ and m₂.
    :param F: The gravitational force between m₁ and m₂.
    :param G: The Gravitational Constant, defaults to 6.67430×10⁻¹¹.
    :return: The mass of the first object
    """
    m1 = F * d ** 2 / (G * m2)
    return m1


def m2(m1: float, d: float, F: float, G: typing.Optional[float] = G) -> float:
    """
    Calculate the mass of the first object.

    :param m1: The mass of the first object in kilograms.
    :param d: The distance between m₁ and m₂.
    :param F: The gravitational force between m₁ and m₂.
    :param G: The Gravitational Constant, defaults to 6.67430×10⁻¹¹.
    :return: The mass of the second object
    """
    m2 = F * d ** 2 / (G * m1)
    return m2


def weight(m: float, g: typing.Optional[float] = constants.GravitationalAcceleration.Earth) -> float:
    """
    Calculate the weight of an object in different Planet.

    :param m: The mass of the object in kilograms.
    :param g: The Gravitational Acceleration, defaults to 9.81 m/s² (Earth Standard).
    :return: The weight of the object in Newtons.
    """
    w = m * g

    return w


def velocity(s: float, t: float) -> float:
    """
    Calculate the velocity of an object.

    :param s: The distance in meters.
    :param t: The time taken to travel a distance 's' in seconds.
    :return: The velocity of the object in m/s.
    """

    v = s / t
    return v


def displacement(v: float, t: float) -> float:
    """
    Calculate the distance covered by an object.

    :param v: The velocity of the object in m/s.
    :param t: The time taken by the object in seconds.
    :return: The displacement in meters
    """

    s = v * t
    return s


def time_required(s: float, v: float) -> float:
    """
    Calculate the time required to travel a distance at a given velocity.

    :param s: The distance in meters.
    :param v: The velocity in m/s.
    :return: The time required to travel the distance in seconds.
    """

    t = s / v
    return t


def acceleration(v: float, t: float) -> float:
    """
    Calculate the acceleration of an object.

    :param v: The velocity of the object in m/s.
    :param t: The time taken by the object to change its velocity in seconds.
    :return: The acceleration of the object in m/s².
    """

    a = v / t
    return a


def time_to_reach_velocity(v: float, a: float) -> float:
    """
    Calculate the time required to reach a certain velocity based on the acceleration.

    :param v: The desired velocity in m/s.
    :param a: The acceleration in m/s².
    :return: The time required to reach the desired velocity in seconds.
    """

    t = v / a
    return t


def force_from_acceleration(m: float, a: float) -> float:
    """
    Calculate the force exerted on an object based on its mass and acceleration.

    :param m: The mass of the object in kilograms.
    :param a: The acceleration of the object in meters per second squared.
    :return: The force exerted on the object in Newtons.
    """

    F = m * a
    return F
