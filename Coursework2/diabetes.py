"""
Please write your name
@author: Harvey Postings

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        try:
            with open(self.filepath, 'r') as file:
                reader = csv.reader(file)
                self.header = next(reader)
                self.data = list(reader)
        except FileNotFoundError:
            raise Exception("File not found")

    def get_dimension(self) -> list:
        num_rows = len(self.data)
        num_cols = len(self.header)
        return [num_rows + 1, num_cols]

    def web_summary(self, filepath: str) -> None:
        summary = {}
        for row in self.data:
            for i, value in enumerate(row):
                if value not in ['Yes', 'No']:
                    continue
                column = self.header[i]
                if column not in summary:
                    summary[column] = {'Yes': 0, 'No': 0}
                summary[column][value] += 1

        with open(filepath, 'w') as file:
            file.write('<html>\n')
            file.write('<head>\n')
            file.write('<title>Diabetes Data Summary</title>\n')
            file.write('</head>\n')
            file.write('<body>\n')
            file.write('<table border="1">\n')
            file.write('<tr>\n')
            file.write('<th>Attribute</th>\n')
            file.write('<th>Yes</th>\n')
            file.write('<th>No</th>\n')
            file.write('</tr>\n')
            for attribute, values in summary.items():
                file.write('<tr>\n')
                file.write('<td>{}</td>\n'.format(attribute))
                file.write('<td>{}</td>\n'.format(values['Yes']))
                file.write('<td>{}</td>\n'.format(values['No']))
                file.write('</tr>\n')
            file.write('</table>\n')
            file.write('</body>\n')
            file.write('</html>\n')

    def count_instances(self, criteria) -> int:
        # delete pass and this line to write your code
        # you can change the parameter criteria or the number of parameters
        # as you want, provided they are explained in doctring for this
        # method
        count = 0
        for row in self.data:
            if all(row[self.header.index(key)] == value for key, value in criteria.items()):
                count += 1
        return count


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    d1.count_instances({'Age': 20})  # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    d2.count_instances({'Age': 30})  # change according to your criteria
