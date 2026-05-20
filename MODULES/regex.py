import re

text = r'''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
456*678*2344

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# '.' period is special character in regex , to search it we need to escape - '\.' . This is followed for all every meta character
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'(Mr|Ms|Mrs)(\.)?\s([A-Z])(\w*)')
# so if we want to search the text without strictly including case we can use re.compile(r'start', re.IGNORECASE) which is flag

matches = pattern.finditer(text) # this is an generator method
# instead of we can use findall which collects only the match if there are no groups, if there is a group it would return only that match 
# if we want to search something in particular we can use pattern.search(text to search)

for match in matches:
    print(match) 
    print(match.group(0)) # this match has a group keyword for which we can access the group by passing index from generator expression
    print(match.groups()) # this prints all the grouped items as a dict

subbed_names = pattern.sub(r'\3\4 \1',text[195:244]) # this can get info from groups in the gen expression so we can get our desired info
print(subbed_names)

regex = r'''

.  - matches to any character except new line
\d - digit (0-9)
\D - not a digit (0-9)
\w - word character (a-z, A-Z, 0-9, _)
\W - not a word character
\s - whitespace (space, tab, newline)
\S - not whitespace

\b - word boundary
\B - not word boundary
^  - beginning of a string i.e ^Start
$  - end of a string i.e end$

[]   - matches characters in brackets , we can use [1-3],[a-z],[a-zA-Z] it matches in the range , '\d\d\d[-.]\d\d\d[-.]\d\d\d\d'
[^ ] - matches characters not in brackets
|    - either or
( )  - group , 'M(r|s|rs)\.?\s+[A-Z]\w*' so it groups the characters and we can search with | so it is there or not checks next one

Quantifiers :
*     - 0 or more , i.e , it matches if the character is there nonce or many times like 'Mr\.?\s+[A-Z]\w*'
+     - 1 or more , i.e , it matches if the character is there once or many times like 'Mr\.?\s+[A-Z]'
?     - 0 or 1 , i.e , it matches the character if its there or not there like 'Mr\.? like if dot is there or not
{3}   - exact number i.e , \d{3}-\d{3}-\d{4}
{3,4} - range of numbers {min,max}

'''