import urllib.request as ur
url = 'http://www.google.com'
conn = ur.urlopen(url)
print(conn)

data  = conn.read()
print(data)
print(conn.status)
print(conn.getheader('Content-Type'))
print('============')
# 讀出header的所有資料
for key, value in conn.getheaders():
    print(key, value)