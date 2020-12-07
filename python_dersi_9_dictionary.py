# key - value  mantığına shiptir...

sehirler = ['kocaeli',"istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("istanbul")])  # eğer dictionary olmasaydı böyle yapacaktık..

#ama bizim istedğimiz :
# print(plakalar["istanbul"]) => 34
# print(plakalar["kocaeli"]) => 41

plakalar = {'kocaeli' : 41, 'istanbul': 34}

print(plakalar["istanbul"])

#eğer yeni değer eklemek istersek;
plakalar['ankara'] = 6
# eğer olan değeri yeni değer atamak istersek;
plakalar['kocaeli'] = 'new value'

print(plakalar)

users = {
    "ahmet" : { "age" : 31,
              "email" : "xyz@outlook.com",
              "gender" : "male" ,
              "roles" : ["admin","user"]},
    "ayşe" : {
           "gender" : "female",
           "age" : 32,
           "email" : "asd@gmail.com",
            "roles": "admin",
    }

}
print(users["ahmet"]["roles"][0])