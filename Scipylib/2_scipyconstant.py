# Constants in scipy: scipy is more focus on scientific implementation, it provides may built in scientific constant: helpfull in data science.
# printing the constant value of PI:
from scipy import constants
print(constants.pi)

# Contsants unit : all list of unit under the constant can be seen with dir() function.
from scipy import constants
print(dir(constants))

# Unit categories : Matric, Binary, Mass,Angle, Time, Length, Presssure,Vloume,Speed, Temperature, Energy, Power, Force.

# Metric (SI) prefixes: yotta
from scipy import constants
print(constants.yotta) # 1e+24
print(constants.zetta) #1e+21
print(constants.exa) #1e+18
print(constants.peta)
print(constants.tera)
print(constants.giga)
print(constants.mega)
print(constants.kilo)
print(constants.hecto)
print(constants.deka)
print(constants.deci)
print(constants.centi)
print(constants.milli)
print(constants.micro)
print(constants.nano)
print(constants.pico)
print(constants.femto)
print(constants.atto)
print(constants.zepto)

# Binary Prefixes: kibi
from scipy import constants
print(constants.kibi) # 1014
print(constants.mebi)
print(constants.gibi)
print(constants.tebi)
print(constants.pebi)
print(constants.exbi)
print(constants.zebi)
print(constants.yobi)

# MASS:  gram
from scipy import constants
print(constants.gram) # 0.001
print(constants.metric_ton)
print(constants.grain)
print(constants.lb)
print(constants.pound)
print(constants.oz)
print(constants.ounce)
print(constants.stone)
print(constants.long_ton)
print(constants.short_ton)
print(constants.troy_ounce)
print(constants.troy_pound)
print(constants.carat)
print(constants.atomic_mass)
print(constants.m_u)
print(constants.u)

# Angle: degree
from scipy import constants
print(constants.degree) #0.0174
print(constants.arcmin)
print(constants.arcminute)
print(constants.arcsec)
print(constants.arcsecond)

# Time:
from scipy import constants
print(constants.minute) # 60.0
print(constants.hour)
print(constants.day)
print(constants.week)
print(constants.year)
print(constants.Julian_year)

# Length : inch
from scipy import constants
print(constants.inch) # 0.0254
print(constants.foot)
print(constants.yard)
print(constants.mil)
print(constants.pt)
print(constants.point)
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstrom)
print(constants.micron)
print(constants.astronomical_unit)
print(constants.light_year)
print(constants.parsec)

# Pressure: pascals
from scipy import constants
print(constants.atm)
print(constants.atmosphere)
print(constants.bar)
print(constants.torr)
print(constants.mmHg)
print(constants.psi)

# Volume : cubic meter
from scipy import constants
print(constants.liter)  #0.001
print(constants.gallon) 
print(constants.gallon_US) 
print(constants.gallon_imp) 
print(constants.fluid_ounce) 
print(constants.fluid_ounce_US) 
print(constants.fluid_ounce_imp) 
print(constants.barrel) 
print(constants.bbl) 


# speed : meter per secs
from scipy import constants
print(constants.kmh)  #0.2777777
print(constants.mph) 
print(constants.mach) 
print(constants.speed_of_sound) 
print(constants.knot)

# Temperature : kelvin
from scipy import constants
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)


# Energy: joules
from scipy import constants
print(constants.eV)
print(constants.electron_volt)
print(constants.calorie)
print(constants.calorie_th)
print(constants.calorie_IT)
print(constants.erg)
print(constants.Btu)
print(constants.Btu_IT)
print(constants.Btu_th)
print(constants.eV)
print(constants.ton_TNT)

# Power : Newton 
from scipy import constants
print(constants.dyn)
print(constants.dyne)
print(constants.lbf)
print(constants.pound_force)
print(constants.kgf)
print(constants.kilogram_force)