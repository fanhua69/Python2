import json

people_string='''
{
    "people":[
        {
            "name": ["John Smith", "Smith2 Horn"],
            "phone":"615-555-7164",
            "emails": {"email1":"johnsmith@bogusemail.com", "email2":"john.smith@work-place.com"},
            "has_license":false
        },
        {
            "mame":"Jane doe",
            "phone":"560-555-5153",
            "emails":null,
            "has_license":true
        },
        {
            "name": "David Fan",
            "sex":  "Male"            
        }
    ],
    
    "cars": [
        "toyota",
        "honda",
        "lexus"
    ]
}
'''

data = json.loads(people_string);


print(type(data))
for k1,v1 in data.items():
    print(f"Name: {k1}", type(v1))
    if type(v1) is dict:
        for key, value in v1.items():
            print(f"\t {key}", end= " ")
            if (type(value) is dict):
                print("\t", end=" ")
                for k, v in value.items():
                    print ("second value:", k, ",", v, end= " " )
                print(" ")
            elif type(value) is list:
                for v in value:
                    print(v, end=",")
                print(" ")
            else:
                print(value)
    else:
        print(v1)