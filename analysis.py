class Analysis:

    def __init__(self, file, id_column, first_value_column, second_value_column):
        self.file = [line.strip().split() for line in open(file).readlines()]
        self.id_column = id_column
        self.first_value_column = first_value_column
        self.second_value_column = second_value_column

    def data_clean(self):
        self.cleaned_data = []

        row_counter = 0
        for row_data in self.file:
            if row_counter == 0 or len(row_data) == 0 or len(row_data) == 1:
                row_counter += 1
                continue
            else:
                self.cleaned_data.append(row_data)

        return self.cleaned_data

    def computation(self):
        self.minimum_id_value = ''
        self.minimum_difference = 9999999999
        for each_row in self.cleaned_data:
            first_value = (each_row[self.first_value_column]).replace('*', '')
            second_value = (
                each_row[self.second_value_column]).replace('*', '')

            if abs(float(first_value) - float(second_value)) < self.minimum_difference:
                self.minimum_id_value = each_row[self.id_column]
                self.minimum_difference = abs(
                    float(first_value) - float(second_value))

        return self.minimum_id_value, int(self.minimum_difference)
