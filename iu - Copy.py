import re
def transform_record(record):
    new_record = re.sub(r',(?=\d)', r',+1-',record)

    return new_record
