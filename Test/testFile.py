
data = b'Hello World\r\n'

# 바이트코드 -> 텍스트
text = data.decode('utf-8')
print(text)
# 텍스트 -> 바이트
data = text.encode('utf-8')
print(data)
# f-String f문자열
name = 'IBM'
shares = 100
price = 91.1
a = f'{name:10s} {shares:10d} {price:10.2f}'
b = f'{name} {shares} {price}'
print(a)
print(b)
c = f'Cost = ${shares * price:0.2f}'
print(c)

names = [ 'Elwood', 'Jake', 'Curtis' ]
nums = [ 39, 38, 42, 65, 111]
line = 'GOOG,100,490.10'
row = line.split(',')
row.insert(2,'aa') #['GOOG', '100', 'aa', '490.10']
print(row)

names.remove('Elwood')
print(names)
del names[0]
print(names)