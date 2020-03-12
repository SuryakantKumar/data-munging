class Extractor:
    """Class for extraction of data"""

    def extract_data(self, file):
        """extraction of raw data file

        param file: File related to analysis
        return extracted_data: Data which has been extracted from raw file
        """
        self.extractd_data = [line.strip().split()
                              for line in open(file).readlines()]
        return self.extractd_data
