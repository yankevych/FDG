from __future__ import absolute_import, unicode_literals

import csv
import random

from project_FDG.celery import app
from .models import ColumnItem, Schema, DataSet
from faker import Faker


@app.task
def aggregate_schema(*args):
    """method that catch all data to start generate data"""
    print(args)
    rows, data_set_pk, schema_pk = args

    schema = Schema.objects.get(pk=schema_pk)
    data_set = DataSet.objects.get(pk=data_set_pk)

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
            row_list = []
            for column in columns:  # generates one fake row and return it
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

            fakewriter.writerow(row_list)
            i += 1
    data_set.file_name = f'{schema.name}_{schema.pk}_{data_set.pk}.csv'
    data_set.status = 'Ready'

    return data_set.save()
    # return requests.post('http://127.0.0.1:8000/gen_ready/', data={'data_set_pk': data_set.pk})
