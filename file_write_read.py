poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

fout = open('relativity.txt', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()
print('===Batch write file complete===')


poem = ''
fin = open('relativity.txt', 'rt')
poem = fin.read()
fin.close()
print(len(poem))
print('===Read file complete===')

poem = ''
fin = open('relativity.txt', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))
print('===Batch Read File Complete===')


poem = ''
fin = open('relativity.txt', 'rt')
for line in fin:
    poem += line

fin.close()
print(len(poem))
print('===Read file using for complete===')
