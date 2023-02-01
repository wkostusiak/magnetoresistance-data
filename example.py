from .functions import separate_pos,position_csv, fast_csv, slow_csv, temp_csv, signs_csv

# working example below #

dane_90st = separate_pos('dane', 90.0144)
dane_0st = separate_pos('dane', 0)

position_csv(dane_0st, 'C:\\Users\\lenovo\\Desktop\\magnetoresistance', 'dane_0', 'dane_0' )
position_csv(dane_90st, 'C:\\Users\\lenovo\\Desktop\\magnetoresistance', 'dane_90', 'dane_90' )

fast_measurement = fast_csv(dane_0st, -0.179859027266502, 'dane_0')
fast_measurement = fast_measurement[4:]
slow_measurement = slow_csv(fast_measurement, dane_0st, 'dane_0')

names = temp_csv(slow_measurement, 'C:\\Users\\lenovo\\Desktop\\magnetoresistance\\dane_0')
signs_csv('C:\\Users\\lenovo\\Desktop\\magnetoresistance\\dane_0', names)

# results in dane_0 and dane_90 dirs in repo #