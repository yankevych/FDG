import mimetypes

from django.http import HttpResponse
from django.shortcuts import render
from .models import Schema, ColumnItem, DataSet
from .tasks import aggregate_schema

COLUMNS = [i[1] for i in Schema.SEPARATORS]
STRINGS = [i[1] for i in Schema.STRINGS]
TYPES = [i[1] for i in ColumnItem.TYPES]

STATUSES = [i[1] for i in DataSet.STATUS]


def schema_view(request):
    """first menu view"""
    schema_list = Schema.objects.all()
    name = request.user.username
    return render(request, 'schema/schema_base.html', {
        'schema_list': schema_list,
        'name': name,
    })


def data_set_view(request, schema_pk):
    """data set view when send generation and GET when reload page"""
    name = request.user.username

    if request.method == 'POST':
        print(request.POST)
        rows = request.POST['schema_rows']
        schema_id = request.POST['schema_id']
        schema = Schema.objects.get(pk=int(schema_id))

        data_set = DataSet.objects.create(schema=schema, status='Create', rows=rows)

        aggregate_schema.delay(rows, data_set.pk, schema.pk)  # CELERY task
        data_set.status = 'Processing'
        data_set.save()

    elif request.method == 'GET':
        schema = Schema.objects.get(pk=schema_pk)

    data_sets = DataSet.objects.filter(schema=schema)
    return render(request, 'data_sets/data_sets_base.html', {
        'data_sets': data_sets,
        'name': name,
        'schema': schema,
    })


def add_column(request):
    """it works when user push ADD button in new schema view"""
    name = request.user.username
    if request.method == 'POST':
        schema = Schema.objects.filter(creator=request.user).last()

        column = ColumnItem.objects.create(
            schema=schema,
            column_type=request.POST['column_type'],
            column_name=request.POST['column_name'],
            order=request.POST['column_order'],
        )
        try:
            if request.POST['column_from']:
                column.range_from = request.POST['column_from']
            if request.POST['column_to']:
                column.range_to = request.POST['column_to']
        except ValueError:
            if request.POST['column_to']:
                column.range_to = request.POST['column_to']
        else:
            pass

        column.save()

        schema_columns = ColumnItem.objects.filter(schema=schema)
        return render(request, 'new_schema/new_schema_base.html', {
            'column_list': COLUMNS,
            'string_list': STRINGS,
            'schema_columns': schema_columns,
            'types': TYPES,
            'name': name,
            'schema': schema,
        })


def delete_column(request):
    """it works when user push delete button in new schema view"""
    name = request.user.username
    if request.method == 'POST':
        schema = Schema.objects.filter(creator=request.user).last()

        column_id = request.POST['column_id']
        column = ColumnItem.objects.get(pk=int(column_id))
        column.delete()

        schema_columns = ColumnItem.objects.filter(schema=schema)
        return render(request, 'new_schema/new_schema_base.html', {
            'column_list': COLUMNS,
            'string_list': STRINGS,
            'schema_columns': schema_columns,
            'types': TYPES,
            'name': name,
            'schema': schema,
        })


def new_schema(request):
    """func that generate new schema view"""
    name = request.user.username
    if request.method == 'GET':
        schema = Schema.objects.create(creator=request.user)
        schema_columns = ColumnItem.objects.filter(schema=schema)

        return render(request, 'new_schema/new_schema_base.html', {
            'column_list': COLUMNS,
            'string_list': STRINGS,
            'schema_columns': schema_columns,
            'types': TYPES,
            'name': name,
            'schema': schema,
        })


def submit_schema(request):
    """func that save schema and load next page view"""
    name = request.user.username
    if request.method == 'POST':
        schema = Schema.objects.filter(creator=request.user).last()
        schema.name = request.POST['schema_name']
        schema.column_separator = request.POST['schema_separator']
        schema.string_character = request.POST['schema_string']
        schema.save()

        data_sets = DataSet.objects.filter(schema=schema)
        return render(request, 'data_sets/data_sets_base.html', {
            'data_sets': data_sets,
            'name': name,
            'schema': schema,
        })


def delete_schema(request):
    """func that DELETE schema after pressed button"""
    if request.method == 'POST':
        schema_id = request.POST['schema_id']
        schema = Schema.objects.get(pk=int(schema_id))
        schema.delete()
        print('del')
    return schema_view(request)


def edit_schema(request):
    """func that EDIT schema after pressed button"""
    name = request.user.username
    if request.method == 'POST':
        schema_id = request.POST['schema_id']
        schema = Schema.objects.get(pk=int(schema_id))
        schema_columns = ColumnItem.objects.filter(schema=schema)
        return render(request, 'new_schema/new_schema_base.html', {
            'column_list': COLUMNS,
            'string_list': STRINGS,
            'schema_columns': schema_columns,
            'types': TYPES,
            'name': name,
        })


def download_data_set(request):
    """function that generate response to download the csv data-set"""
    if request.method == 'POST':
        data_set_id = request.POST['data_set_id']
        data_set = DataSet.objects.get(pk=data_set_id)

        full_path = 'media/' + data_set.file_name
        fl = open(full_path, 'r')
        mime_type, _ = mimetypes.guess_type(full_path)
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % data_set.file_name
        return response
