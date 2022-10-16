import re

result = re.search(r'(\w*), (\w*)', 'lovelace, ada hello, shubham')
print(result.groups())

print("{} is match found.\n{} and {} are the groups found".format(result[0], result[1], result[2]))