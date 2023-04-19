import datetime
from physics import gravity
from . import constants

__name__ = "physicsKit"
__description__ = "A Python library for Physics calculations!"
__version__ = "1.0.0"
__author__ = "Sayad Uddin Tahsin"
__author_email__ = "mr.pluto012@gmail.com"
__copyright__ = f"© Copyright 2023 {('- ' + str(datetime.datetime.today().year) + ' ') if int(datetime.datetime.today().year) != 2023 else ''}Sayad Uddin Tahsin."
__license__ = "MIT"

GravitationalAcceleration = constants.GravitationalAcceleration
