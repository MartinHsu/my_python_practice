import sys

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    out_str = 'value= ' + value + ', name= ' + name + ', value2= ' + value2
    print(out_str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

