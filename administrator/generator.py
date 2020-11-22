import csv
import random
from .models import ColumnItem
from faker import Faker


def aggregate_schema(rows, data_set, schema):
    """method that first catch all data to start generate data"""
    print(rows)
    if schema.column_separator == 'Comma (,)':
        delimiter = ','
    else:
        delimiter = '.'

    if schema.string_character == 'Double-quote (")':
        quotechar = '"'
    else:
        quotechar = "'"

    columns = ColumnItem.objects.filter(schema=schema)
    with open(f'media/{schema.name}_{schema.pk}_{data_set.pk}.csv', 'w', newline='') as f:
        fakewriter = csv.writer(f, delimiter=delimiter, quotechar=quotechar)

        headers_row = [column.column_name for column in columns]
        fakewriter.writerow(headers_row)
        print(headers_row)
        for i in range(0, int(rows)):
            fakewriter.writerow(generate_row(columns))
            i += 1

    data_set.status = 'Ready'
    data_set.file_name = f'{schema.name}_{schema.pk}_{data_set.pk}.csv'
    data_set.save()


def generate_row(columns):
    """method generates one fake row and return it to main"""
    print('55')

    row_list = []
    for column in columns:
        fake = Faker()
        if column.column_type == 'Full name':
            data = fake.name()
        elif column.column_type == 'Integer':
            data = random.randint(column.range_from, column.range_to)
        elif column.column_type == 'Job':
            data = fake.job()
        elif column.column_type == 'Company name':
            data = fake.company()
        elif column.column_type == 'Date':
            data = fake.date_time().date()

        row_list.append(data)

    print(row_list)
    return row_list






