import re 
log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


print(re.search(r'a.e.i', 'academia'))
print(re.search(r'^a.e.i', 'a-e-i->this is me'))
print(re.search(r'a.e.i$', 'academia_is a e i'))