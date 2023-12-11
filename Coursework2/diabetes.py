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
        return [num_rows, num_cols]

    def web_summary(self, filepath: str) -> None:
        summary_positive = {}
        summary_negative = {}
        # Iterate over the rows in the data
        for row in self.data:
            for i, value in enumerate(row):
                if value not in ['Yes', 'No']:
                    continue
                column = self.header[i]
                if column not in ['Age', 'Gender']:
                    # If the class is positive, add to the positive summary
                    if row[self.header.index('class')] == 'Positive':
                        if column not in summary_positive:
                            summary_positive[column] = {'Yes': 0, 'No': 0}
                        summary_positive[column][value] += 1
                    # If the class is negative, add to the negative summary
                    else:
                        if column not in summary_negative:
                            summary_negative[column] = {'Yes': 0, 'No': 0}
                        summary_negative[column][value] += 1

        with open(filepath, 'w') as file:
            file.write('<html>\n')
            file.write('<head>\n')
            file.write('<title>Diabetes Data Summary</title>\n')
            file.write('</head>\n')
            file.write('<body>\n')
            file.write('<table border="1" width="100%" style="font-family:'
                       'Arial; text-align: center;">\n')
            file.write('<tr bgcolor="green" style="color: white;">\n')
            file.write('<th rowspan="3">Attribute</th>\n')
            file.write('<th colspan="4">Class</th>\n')
            file.write('</tr>\n')
            file.write('<tr bgcolor="green" style="color: white;">\n')
            file.write('<th colspan="2">Positive</th>\n')
            file.write('<th colspan="2">Negative</th>\n')
            file.write('</tr>\n')
            file.write('<tr bgcolor="green" style="color: white;">\n')
            file.write('<th>Yes</th>\n')
            file.write('<th>No</th>\n')
            file.write('<th>Yes</th>\n')
            file.write('<th>No</th>\n')
            file.write('</tr>\n')
            # Iterate over the attributes in the positive summary
            for attribute in summary_positive.keys():
                file.write('<tr>\n')
                # Write the attribute name
                file.write('<td>{}</td>\n'.format(attribute))
                # Write the values for the attribute
                file.write('<td>{}</td>\n'.format(
                    summary_positive[attribute]['Yes']))
                file.write('<td>{}</td>\n'.format(
                    summary_positive[attribute]['No']))
                # If the attribute is in the negative summary,
                # write the values
                file.write('<td>{}</td>\n'.format(summary_negative.get(
                    attribute, {}).get('Yes', 0)))
                file.write('<td>{}</td>\n'.format(summary_negative.get(
                    attribute, {}).get('No', 0)))
                file.write('</tr>\n')
            for attribute in summary_negative.keys():
                if attribute not in summary_positive:
                    file.write('<tr>\n')
                    file.write('<td>{}</td>\n'.format(attribute))
                    file.write('<td>{}</td>\n'.format(0))
                    file.write('<td>{}</td>\n'.format(0))
                    file.write('<td>{}</td>\n'.format(
                        summary_negative[attribute]['Yes']))
                    file.write('<td>{}</td>\n'.format(
                        summary_negative[attribute]['No']))
                    file.write('</tr>\n')
            file.write('</table>\n')
            file.write('</body>\n')
            file.write('</html>\n')

    def count_instances(self, criteria) -> int:
        """
        Counts the number of instances in the
        dataset that match the given criteria
        
        The criteria should be provided as a dictionary where the keys are
        the column names and the values are the attribute values to match.
        
        The method returns the total count of matching instances.
        
        For example, if the criteria is {"Age": 55, "Polyuria": "Yes"},
        the method will return the number of instances where
        the Age is 55 and Polyuria is Yes.
        
        For this example you would use the method like this:
            d = Diabetes("diabetes_data.csv")
            count = d.count_instances({"Age": 55, "Polyuria": "Yes"})
            print(count) # Prints the number of matching instances
        """
        count = 0
        for row in self.data:
            # Compares header to criteria keys and
            # then compares row to criteria values
            if all(str(row[self.header.index(key)]) == str(value)
                   for key, value in criteria.items()):
                count += 1
        return count


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    d1.count_instances({"class": 'Negative', 'Polyuria': 'Yes'})
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    d2.count_instances({"Age": 55})
    print()

    # test diabetes3_data.csv
    d3 = Diabetes("diabetes3_data.csv")
    print(d3.get_dimension())
    d3.web_summary('stat03.html')
    d3.count_instances({"Age": 55, "Polyuria": "Yes"})