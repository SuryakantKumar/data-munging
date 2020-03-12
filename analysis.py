from data_extract import Extractor


class Analysis:
    """Class for analysis of data"""

    def __init__(self, file, id_column, first_value_column, second_value_column):
        """Initializing the analysis class with related columns

        param id_column: column having id or name
        param first_value_column: column having first value for difference
        param second_value_column: column having second value for difference
        """
        self.extractor = Extractor()
        self.file = self.extractor.extract_data(file)
        self.id_column = id_column
        self.first_value_column = first_value_column
        self.second_value_column = second_value_column

    def data_clean(self):
        """Removing first row because it's a header and rows having zero or one values,
        because we require atleast three rows for finding difference """

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
        """Computing the id value with minimum difference"""

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
