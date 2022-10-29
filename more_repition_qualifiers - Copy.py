import re

print(re.search(r'[a-z]{5}', 'a ghost'))
print(re.findall(r'\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))
print(re.findall(r'[\w]{5,10}', 'I really like strawberries'))
print(re.findall(r'[\w]{5,}', 'I really like strawberries'))
print(re.findall(r's\w{,20}', 'I really like strawberries'))



def extract_pid(log_line):
    """Code to extract process id followed by an UPPERCASE message"""
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
