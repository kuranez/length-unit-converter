# Length Unit Converter

# Version: 0.1
# Author: github.com/kuranez

# ------------------------------------------------------------------------------
# Längenmaße in unterschiedliche Einheiten konvertieren
# ------------------------------------------------------------------------------
                                                                                  #--------------------------------------------------
def convert_length(value: float, unit_input: str, unit_output: str) -> float:     #              def --> Funktion definieren        #
                                                                                  #--------------------------------------------------
    unit = {  'm'   : 10**0,    'dm'   : 10**-1,    'nm' : 10**-9,                    # def funktionsname(arguments):
              'dam' : 10**1,    'cm'   : 10**-2,    'pm' : 10**-12,
              'hm'  : 10**2,    'mm'   : 10**-3,    'fm' : 10**-15,                                     # Parameter:
              'km'  : 10**3,    'my_m' : 10**-6,                                                            #p_name: typ

              'angstroem' : 10**-10,                                                                    # Beispiele:
                                                                                                            #value: float
              'mile' : 1609.344,    'sm' : 1852,                                                                  #  Gleitkommazahl
              'yd'   : 0.9144,      'ft' : 0.3048,    'inch': 2.54 * 10**-2}                                #input: str
                                                                                                                  #  String/Text
    return value * unit[unit_input] / unit[unit_output]                           #--------------------------------------------------
                                                                                  #                    Dictionaries                 #
                                                                                  #--------------------------------------------------
                                                                                  #            variable = { 'string': any, usw. }   #
                                                                                  #--------------------------------------------------


