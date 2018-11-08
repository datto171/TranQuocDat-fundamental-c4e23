import pyexcel as p 
records = p.iget_records(file_name="your_file.xls")
for record in records:
    print("%s is aged at %d" % (record['title'], record['number']))
p.free_resources()
