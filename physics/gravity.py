import math
import typing
from physics import constants


def Gforce(m1: float, m2: float, d: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational force between two objects.

    :param m1: The mass of the first object in kilograms.
    :param m2: The mass of the second object in kilograms.
    :param d: The distance between the two objects in meters.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The gravitational force between the two objects in Newtons.
    """

    F = G * ((m1 * m2) / (d ** 2))
    return F


def distance(m1: float, m2: float, F: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the distance between two objects.

    :param m1: The mass of the first object in kilograms.
    :param m2: The mass of the second object in kilograms.
    :param F: The gravitational force between m₁ and m₂.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The distance between m₁ and m₂ in Meters.
    """

    d = math.sqrt((G * m1 * m2) / F)
    return d


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


def m1(m2: float, d: float, F: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the mass of the first object.

    :param m2: The mass of the second object in kilograms.
    :param d: The distance between m₁ and m₂.
    :param F: The gravitational force between m₁ and m₂.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The mass of the first object
    """

    m1 = F * d ** 2 / (G * m2)
    return m1


def m2(m1: float, d: float, F: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the mass of the first object.

    :param m1: The mass of the first object in kilograms.
    :param d: The distance between m₁ and m₂.
    :param F: The gravitational force between m₁ and m₂.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The mass of the second object
    """

    m2 = (F * d ** 2) / (G * m1)
    return m2


def weight(m: float, g: typing.Optional[float] = constants.GravitationalAcceleration.Earth) -> float:
    """
    Calculate the weight of an object in different Planet.

    :param m: The mass of the object in kilograms.
    :param g: The gravitational acceleration in m/s², defaults to 9.81 m/s² (Earth Standard).
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


def force(m: float, a: float) -> float:
    """
    Calculate the force exerted on an object based on its mass and acceleration.

    :param m: The mass of the object in kilograms.
    :param a: The acceleration of the object in meters per second squared.
    :return: The force exerted on the object in Newtons.
    """

    F = m * a
    return F


def gravitational_potential_energy_at_height(m: float, h: float, g: typing.Optional[float] = constants.GravitationalAcceleration.Earth) -> float:
    """
    Calculates the amount of energy an object possesses due to its position in a gravitational field.

    :param m: The mass of the object in kilograms.
    :param h: The height of the object above a reference point in meters.
    :param g: The gravitational acceleration in m/s², defaults to 9.81 m/s² (Earth Standard).
    :return: The gravitational potential energy of the object in Joules.
    """

    U = m * g * h
    return U



def gravitational_energy_between_two_masses(m1: float, m2: float, d: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational potential energy between two objects.

    :param m1: The mass of the first object in kilograms.
    :param m2: The mass of the second object in kilograms.
    :param d: The distance between the two objects.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The gravitational potential energy between the two objects.
    """

    U = -G * m1 * m2 / d
    return U


def escape_velocity(m: float, r: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculates the minimum velocity required for an object to escape the gravitational field of a celestial body.

    :param m: The mass of the celestial body in kilograms.
    :param r: The radius of the celestial body in meters.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The escape velocity in meters per second.
    """

    ve = math.sqrt(2 * G * m / r)
    return ve


def period_of_orbit(r: float, M: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculates the period of an object in circular orbit around a central mass.

    :param r: The radius of the orbit in meters.
    :param M: The mass of the central body in kilograms.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The period of the orbit in seconds.
    """

    T = 2 * math.pi * math.sqrt(r ** 3 / (G * M))
    return T


def orbital_velocity(r: float, M: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculates the orbital velocity of an object in circular orbit around a central mass.

    :param r: The radius of the orbit in meters.
    :param M: The mass of the central body in kilograms.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The orbital velocity of the object in meters per second.
    """

    v = math.sqrt(G * M / r)
    return v


def gravitational_potential(m: float, r: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational potential energy.

    :param m: The mass of the object in kilograms.
    :param r: The distance from the object in meters.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The gravitational potential energy in Joules.
    """

    V = -(G * m) / r
    return V


def gravitational_field_strength(M: float, r: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational field strength.

    :param M: The mass of the object in kilograms.
    :param r: The distance from the object in meters.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The gravitational field strength in Newtons per kilogram.
    """

    g = G * M / r ** 2
    return g


def gravitational_acceleration(m: float, r: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational acceleration.

    :param m: The mass of the object in kilograms.
    :param r: The distance from the object in meters.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The gravitational acceleration in meters per second squared.
    """

    a = G * m / r ** 2
    return a


def gravitational_time_dilation(dT: float, M: float, r: float, c: typing.Optional[float] = constants.c, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational time dilation.

    :param dT: The proper time interval.
    :param M: The mass of the object in kilograms.
    :param r: The distance from the object in meters.
    :param c: The speed of light, defaults to 299792458 m/s.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The gravitational time dilation in seconds.
    """

    delta_t = dT * math.sqrt(1 - (2 * G * M) / (c ** 2 * r))
    return delta_t


def schwarzschild_radius(M: float, c: typing.Optional[float] = constants.c, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the Schwarzschild radius.

    :param M: The mass of the object in kilograms.
    :param c: The speed of light, defaults to 299792458 m/s.
    :param G: The Gravitational Constant, defaults to 6.67430 × 10⁻¹¹.
    :return: The Schwarzschild radius in meters.
    """

    r = (2 * G * M) / c ** 2
    return r


def gravitational_redshift(r1: float, r2: float, M: float, c: typing.Optional[float] = constants.c, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the gravitational redshift.

    :param r1: The initial distance from the object in meters.
    :param r2: The final distance from the object in meters.
    :param M: The mass of the object in kilograms.
    :param c: The speed of light in meters per second. Default is 299792458.0 m/s.
    :param G: The gravitational constant. Default is 6.67430 × 10⁻¹¹.
    :return: The gravitational redshift.
    """

    z = (1 - (2 * G * M) / (c ** 2 * r2)) / (1 - (2 * G * M) / (c ** 2 * r1)) - 1
    return z


def chandrasekhar_limit(xi: float, solar_mass: float = 1.9885e30) -> float:
    """
    Calculate the Chandrasekhar limit for a given value of xi.

    :param xi: The dimensionless constant xi.
    :param solar_mass: The mass of the sun in kg (default: 1.9885e30).
    :return: The Chandrasekhar limit in kg.
    """

    M = (1.44 * solar_mass) / (xi**2)
    return M


def roche_limit(R: float, rho1: float, rho2: float) -> float:
    """
    Calculate the Roche limit, which is the minimum distance between two celestial bodies at which one will be destroyed by tidal forces.

    :param R: The radius of the primary body in meters.
    :param rho1: The density of the primary body in kg/m³.
    :param rho2: The density of the secondary body in kg/m³.
    :return: The Roche limit in meters.
    """

    return R * ((2 * rho2) / rho1) ** (1/3)


def geostationary_orbit(T: float, M: float, G: typing.Optional[float] = constants.G) -> float:
    """
    Calculate the radius of a geostationary orbit.

    :param T: The period of the orbit in seconds.
    :param M: The mass of the planet in kilograms.
    :param G: The gravitational constant. Default is 6.67430 × 10⁻¹¹.
    :return: The radius of the orbit in meters.
    """

    return ((G * M * T ** 2) / (4 * math.pi ** 2)) ** (1/3)
