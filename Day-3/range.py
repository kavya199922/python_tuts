#JSON
import json
str1={
    23:{
    'name':'Jonas',
    # 'eid':23,
    'email':'jonas23@gmail.com',
    'role':'manager'
    },
47:{
    'name':'Martha',
    # 'eid':47,
    'email':'martha47@gmail.com',
    'role':'Team Lead'
    }
}
print(type(str1))
#serialization:JSON->Python
str_format=json.dumps(str1)
print(str_format)
print((type(str_format)))
with open("dat_json.json","w") as write:
    json.dump(str1,write,indent=5)

