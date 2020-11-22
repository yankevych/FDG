import csv
import random
from calendar import calendar
from datetime import date
from .models import ColumnItem
import requests
import names
from faker import Faker


def aggregate_schema(rows, empty_schemas):
    """method that first catch all data to start generate data"""
    print('66')
    print(rows)
    for schema in empty_schemas:
        print('11')
        with open(f'{schema.name}{schema.pk}.csv', 'w', newline='') as f:
            print('1223333')
            spamwriter = csv.writer(f)
            print(spamwriter)
            print('22')
            for i in range(0, int(rows)):
                print(i)
                columns = ColumnItem.objects.filter(schema=schema)
                spamwriter.writerow(generate_row(columns))
                i += 1


def generate_row(columns):
    """method generates one row"""
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






