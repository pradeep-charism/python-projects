import re

text = "this is a good day abc sdfd"
if re.search("good", text):
    print("su")
else:
    print("fl")

re.split("a", text)

print(re.findall('(abc)', text))

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.findall('\w{2} \d{5}(\(\d{4}\)|-\d{4})', "MI 12345 6789 MI 12345-6789 MI 12345(6789) MI 12345-(6789)"))

result = re.findall("[a-zA-Z][0-9]*", " www.aBC.com")
print(result)

import re

string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

s = 'ACBCAC'
print(re.findall('^AC', s))

s = 'ACAABAACAAAB'
result = re.findall('A{1,2}', s)
print(result)
L = len(result)
print(L)

s = 'ZAZACAABAACAAAB'
print(re.findall('(?<=[ZAZ])*', s))

contacts = "Office of Research Administration: (734) 647-6333 | 4325 North Quad\
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205\
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500\
Office of the Dean: (734) 647-3576 | 4322 North Quad\
UMSI Engagement Center: (734) 763-1251 | 777 North University\
Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad"
print(contacts)

phone_numbers = re.findall('[(]\d{3}[)]\s\d{3}[-]\d{4}', contacts)
print(phone_numbers)

url_texts = "'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'"
domain = re.findall('(?<=[https]:\/\/)([A-Za-z0-9.]*)', url_texts)
print(domain)

text = r'''Everyone has the following fundamental freedoms:
    (a) freedom of conscience and religion;
    (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
    (c) freedom of peaceful assembly; and
    (d) freedom of association.'''

pattern = '\(.\)'
print(len(re.findall(pattern, text)))

print(r'\ttab')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


# pattern = re.compile(r'coreyms\.com')
pattern = re.compile(r'\W')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)




