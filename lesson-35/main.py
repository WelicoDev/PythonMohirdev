import json

x=10
x_json = json.dumps(x)

y=5.5
y_json = json.dumps(x)

# print(type(x_json))

m=True
m_json = json.dumps(m)

# print(m_json)
# print(type(m_json))

sonlar = (12 , 24 , 38 , 44)
sonlar_json = json.dumps(sonlar)

# print(type(sonlar))

# print(sonlar_json)
# print(type(sonlar_json))

print(m_json)

print(json.loads(m_json))
print(json.loads(sonlar_json))