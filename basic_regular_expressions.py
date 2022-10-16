import re

print(re.search(r'[a-z]way', 'The end of the highway'))
print(re.search(r'[a-z]way', 'The end of the high way'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))

def check_punctuation (text):
    # This code checks for punctutation marks in the passed text
    result = re.search(r"[,.;?!]", text)
    return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# To search for characters that aren't in the text
print(re.search(r'[^a-zA-Z]', 'A sentence having spaces and other things.'))
print(re.search(r'[^a-zA-Z ]', 'A sentence having spaces and other things.'))

print(re.findall(r'cat|dog', 'I like both cats and dogs'))
print(re.search(r'cat|dog', 'I like both cats and dogs'))

# To search for a pattern having n number of characters in between
# Repetition qualifiers
print()
print(re.search(r'Py.*n', "Python programming"))
print(re.search(r'Py.*n', "Pyn"))
print(re.search(r'Py[a-z]*n', "Python programming"))

print()
# + expression checks one or more occurrence of the character before it
print(re.search(r'o+l+', 'woolly'))
print(re.search(r'o+l+', 'molly'))
# ? expression checks 0 or one occurence of the character before it
print(re.search(r'p?each', 'To each their own'))
print(re.search(r'p?each', 'have some peach'))

# escape characters
print(re.search(r'\.com', 'google.com')) # using \ to check for .com occurence
print(re.search(r'\w*', 'This is an example')) # \w is used to check for alphanumeric characters including '_'
print(re.search(r'\w*', 'And_this_is_another'))

# \d -> digits. \s -> white spaces, \b -> word boundaries

def is_valid_variable_name(text):
    return re.search(r'^[a-zA-z_]\w*$', text) != None

print(is_valid_variable_name('my_variable'))
