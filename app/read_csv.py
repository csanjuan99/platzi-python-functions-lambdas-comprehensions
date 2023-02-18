import csv


def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row


def transforming_data(path):
    data_countries = []
    data_csv = read_csv(path)
    columns = next(data_csv)
    for row in data_csv:
        country = dict(zip(columns, row))
        data_countries.append(country)
    return data_countries


if __name__ == '__main__':
    path = './data.csv'
    data = transforming_data(path)
