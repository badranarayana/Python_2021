"""
Strings:
--> string is sequence of characters
--> string is immutable object(can't manipulate it)

-->  How do we define string in python?


syntax:
  1) single quote ''
  2) double quote  " "
  3) tipple quite """ """
  

Note: in compiled languages char type there, but in python everything is string no char type separately.


Built-in methods
---------------
str methods:

 | capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
"""



# group of English chars
# 123
# True or False




# Example
name = "Badra"
location = "Hyderabad"
email = "admin@gmail.com"



# How do we access each char from string?
# Note: stores data with index value
name = "Badra"

print(type(name))
print(help(''))
# fecth first char 'B'

# Indexing
print(name[0])


#
name = 'badra  narayana'
capital_name = name.capitalize()  #  retuns new version string, source string won't modified(it is immutable object)
print(name) #  original
print(capital_name)
print(len(name))

# upper case
location = "hyderabad"

# HYDERABAD
upper = location.upper()
print(location)
print("Upper:", upper)


# lower
location = "HYDEraBad"
# "hyderabad"
lower = location.lower()
print("original", location)
print("lower", lower)

# title
name = "badra narayan reddy"
# "Badra Narayan"
title = name.title()
print(name)
print(title)
print("************ count *****************")

my_name = "Badra jdlkdlldlkaml lkdklmasldmlas  123badra31231qddada klldlamdla"
print(my_name.count("Badra"))


print("********************** Index ************************")
color = "yellow blue yellow"
print("index", color.index("blue"))
# 4

print("****************** lstrip and rstrip and strip *****************")

name = "     badra narayan "
print(name)
print(name.lstrip())
print(name.rstrip())
# 3 lines
out = name.lstrip()
out = out.rstrip()
print(out)
print("strip", name.strip()) # removes leading and trailing spaces in string

print("*************************** split *********************")

name = "raja|22|20000|hyderabad"
out = name.split('|')  # list of strings

first_name = out[0]
age = out[1]
salary = out[2]
location = out[3]


print("**************** find ****************")

school_name = "Zph high school"
print(school_name.find("school")) # return -1 in case sub not found
#print(school_name.index("School")) # raises exception(valieError) if given sub string not found



print("***************** format ******************")
temaple = """Greeting from client {client_name}
             My dear Employee {name}
""" # Hi Name

print(temaple)
name = "Badra"

data = temaple.format(name=name, client_name="HCL")
print(data)


print(temaple.format(name="ABC", client_name="gxgxg"))




# Write a progam to send birthday wishes to your on today
birth_days = ['Mani', 'Srinu', "raja"]

birth_day_template = """
Hi mr. {name}

Manay more happy returns of the day and good luck

thanks & Regards,
{company_name}
"""

birth_day_template_1 = """
Hi mr. {1}

Manay more happy returns of the day and good luck

thanks & Regards,
{0}
"""

for name in birth_days:
    formated_template = birth_day_template.format(name=name, company_name="Wipro")
    print(formated_template)



# By using f stings
school = "Zph high school"

location = "Guntur"

school_address = f'School {school} located at {location}'
print("f strings", school_address)
school_address = 'School {school} located at {location}'.format(school=school, location=location)
print("format: ", school_address)


# by using %

price = "Price: %.3f - quantity: %d"

print(price % (123, 22))





# How many ways we can format a give string

# f string
name = "Mani"
last_name = "G"
greeting_text = f"All the best mr. {name} - {last_name}"
print(greeting_text)

# by using format explicit index
greeting_text = "All the best mr. {1} - {0}"

print(greeting_text.format(name, "G"))

# by using format implicit index position
greeting_text = "All the best mr. {} - {}"

print(greeting_text.format("G", name))

# by using string moduling %
greeting_text = "All the best mr. %s - %s"

print(greeting_text % ("G", name))

#greeting_text.is

print("************************* join **************************")

# list name ['first_name', 'last_name']

data = ['Badra', "A", "abc", "cdg"]

# create a string from this data object

full_name = ' $ '.join(data)
print(full_name)

plus = "+-------------------"

print(plus.join(data))

colors = ('red', 'green', 'yellow', 'blue')

# red ----> green ----> yellow ---> blue
symbol = ""
print("".join(colors))

# Join takes iterable object and concatenate each item in it with string

colors = ('red', 'green', 'yellow', 'blue')



def join(iterable, sysmbol):
    # FUnctions in python
    out = ""
    symbol = sysmbol
    for index, color in enumerate(iterable):
        if index <= len(iterable) - 2 :  # 4 -1 = 3
            out = out + color + symbol  # "" + "--" + red  --->red
        else:
            print("ELase")
            out = out + color

    print(out)

join(iterable=['Badra', 'Narayana', 'reddy'], sysmbol=" ***********  ")


# -----------------------------------------------------------------------------------------------------------


# Write a program to reverse a string?

company = "Badra Software Technologies"

# See how it will in reverse order

# approach #1
# using built in ones
data = list(reversed(company))
print(data)
rev_string = "".join(data)
print(rev_string)


# write in single line:
re_string = "".join(list(reversed(company)))
print(re_string)

# # approach #2 using slicing

print(company[::-1])


# approach #3 our custom logic
#"Badra"

company = "Badra Software Techonologies"
rev_str = ''
length = len(company)
indexs = range(1, length + 1) # 1 to 27 numbers
for i in indexs: # i =2
    rev_str += company[-i] # [-2]
print(rev_str)


company="ABDCEF"
rv = ''
for i in reversed(range(-len(company), 0)):
    #print(i)
    rv += company[i]

print("OUT", rv)



# Write a program to find all digites from a list?

#data = ['abcms', '1233', 'xyck123', '8888']


salary = "           wjsjjsjs123443" # "123".

print(" Before strip", len(salary))
salary = salary.strip().upper() # "wjsjjsjs123443".upper() -->
print(" after strip:  ", len(salary))

# alpha numaric or digits

print("isalnum", salary.isalnum())
print("isalpha", salary.isalpha())
print("isdecimal", salary.isdecimal())
print("isnumeric", salary.isnumeric())
print("isupper", salary.isupper())
print("isspace", salary.isspace())



# encode and decode
data = "SoftWare 25525252"
print(type(data))
print(data.encode(encoding="UTF-8"))



name = b'SoftWare 25525252'
print(type(name))
print(name.decode())



# How do you convert string to byte string

data = "abc qweee"
byte_date = data.encode("utf-8")
print(byte_date)


# how do you convert bytes to string?
data = b"hello world"
str_data = data.decode('utf-8')
print(str_data)




# encoding and decoding work on code we provide

# UTF-8, UTF-15

data = "ZPH school"
# converting into bytes(str --> bytes)
data = data.encode(encoding="utf-8")
print(data)
# decode the encoded string(bytes --> str)
data = data.decode(encoding="utf-8")
print(data)












































