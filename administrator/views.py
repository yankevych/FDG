from django.shortcuts import render, redirect
from .models import Schema, ColumnItem
from .generator import aggregate_schema


def schema_view(request):
    schema_list = Schema.objects.all()
    return render(request, 'schema/schema_base.html', {'schema_list': schema_list})


def new_schema(request):
    """"""
    columns = [i[1] for i in Schema.SEPARATORS]
    strings = [i[1] for i in Schema.STRINGS]
    types = [i[1] for i in ColumnItem.TYPES]
    if request.method == 'POST':
        schema = Schema.objects.filter(creator=request.user).last()

        ColumnItem.objects.create(
            schema=schema,
            column_type=request.POST['column_type'],
            column_name=request.POST['column_name'],
            order=request.POST['column_order'],
            range_from=request.POST['column_from'],
            range_to=request.POST['column_to'],
        )

        schema_columns = ColumnItem.objects.filter(schema=schema)

    else:
        schema = Schema.objects.create(creator=request.user)
        schema_columns = ColumnItem.objects.filter(schema=schema)

    return render(request, 'new_schema/new_schema_base.html', {
        'column_list': columns,
        'string_list': strings,
        'schema_columns': schema_columns,
        'types': types,
    })


def submit_schema(request):
    """"""
    # if request.method == 'POST' and not request.POST['schema_rows']:
    if request.method == 'POST':
        print('11')
        try:
            print('22')
            rows = request.POST['schema_rows']
            print(rows)
            print('223')
            empty_schemas = Schema.objects.filter(creator=request.user, status='Create')
            print(empty_schemas)
            aggregate_schema(rows, empty_schemas)
        except:
            print('33')
            schema = Schema.objects.filter(creator=request.user).last()
            schema.name = request.POST['schema_name']
            schema.column_separator = request.POST['schema_separator']
            schema.string_character = request.POST['schema_string']
            schema.save()
        finally:
            schemas = Schema.objects.filter(creator=request.user)
            return render(request, 'data_sets/data_sets_base.html', {
                'schemas': schemas,
            })
    # elif request.method == 'POST' and request.POST['schema_rows']:


    else:
        pass






