from .functions import separate_position,position_csv, fast_separate, slow_separate, separate_temp


dane_90st = separate_position('dane', 90.0144)
dane_0st = separate_position('dane', 0)

parent_var = 'C:\\Users\\lenovo\\Desktop\\ziombal'

position_csv(dane_0st, 'C:\\Users\\lenovo\\Desktop\\ziombal', 'dane_0', 'dane_0_all' )
position_csv(dane_90st, 'C:\\Users\\lenovo\\Desktop\\ziombal', 'dane_90', 'dane_90_all' )

fast_measurement = fast_separate(dane_0st, -0.179859027266502, 'dane_0')
fast_measurement = fast_measurement[4:] # manually checked the data --> first 4 rows had to be deleted #
slowmeasurement = slow_separate(fast_measurement, dane_0st, 'dane_0')

separate_temp(slowmeasurement, dirname='dane_0')