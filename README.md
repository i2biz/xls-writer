Utility for generating tables
=============================

[![Build Status](https://travis-ci.org/i2biz/xls-writer.svg?branch=master)](https://travis-ci.org/i2biz/xls-writer)


Sometimes you need to create 50 column xls file for to integrate with external system,
you already have data in Python format. 

This library strives to make this easier. 

Example
-------

Imports: 

    
    import csv
    import io
    
    from xls_writer import api, utils, csv_formatter
    from xls_writer.field import FieldFactory

We'll format following data source (as you see some rows are missing datum). 

    class Bar(object):
        def __init__(self, canary):
          self.baz = canary
        
    DATA = [
        {"foo": "1", "bar": Bar("row 1")},
        {"foo": "2", "bar": Bar("row 2")},
        {"foo": 3}
    ]
    
    
Table description looks like that. It's an immutable object that describes the table, and
how the data is loaded. 

Column values can either constants or be read from row object (which can be a dir or a plain
python object).               
    

    fields = [
        FieldFactory("Foo Header", required=True).path("foo").type_formatter(int).create(),
        FieldFactory("Bar Header", required=False, default="<<Missing>>")
        .path("bar.baz").type_formatter(str).create(),
        FieldFactory.create_const_field("Description", "Refer to terms and conditions"),
        FieldFactory.create_const_field("Custom Field 123", "")
      ]
      
    table_description = api.TableDescription(fields=fields)
    
Now we'll format data source to file: 
    
    file = io.StringIO()
    
    formatter = csv_formatter.CSVFormatterFactory(dialect=csv.excel_tab)
    utils.store_table(source_data, table_description, formatter, file, close_file_on_finish=False)
    file.seek(0)
    print(str(file.read(-1)))

This should print: 
    
    Foo Header    Bar Header    Description    Custom Field 123
    1    row 1    Refer to terms and conditions
    2    row 2    Refer to terms and conditions        
    3    <<Missing>>    Refer to terms and conditions
    
See more examples in tests.     
          
