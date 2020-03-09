from analysis import Analysis


class WeatherAnalysis(Analysis):

    def __init__(self, file, id_column=0, first_value_column=1, second_value_column=2):
        super().__init__(file, id_column, first_value_column, second_value_column)


result = WeatherAnalysis(
    '/Users/suryakantkumar/MountBlueSpace/2020.03.07/Data-Munging/weather.dat')
result.data_clean()
print('Day Number : ', result.computation()[0])
print('Smallest Temperature Spread : ', result.computation()[1])
