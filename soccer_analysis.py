from analysis import Analysis


class SoccerAnalysis(Analysis):

    def __init__(self, file, id_column=1, first_value_column=6, second_value_column=8):
        super().__init__(file, id_column, first_value_column, second_value_column)


result = SoccerAnalysis(
    '/Users/suryakantkumar/MountBlueSpace/2020.03.07/Data-Munging/football.dat')
result.data_clean()
print("Team : ", result.computation()[0])
print("Minimum Difference : ", result.computation()[1])
