info = {"hello": "irfan",
        "welcome": "to bangalore",
        "company": "Amadeus"
        }
#prints only the key
for item in info:
    print item

print info

#-------------------------------------------------------------------------------------

for item in info:
    print item,"->" ,info[item]

for k,v in info.iteritems():
    print k, "its value is", v


import io
print (io.DEFAULT_BUFFER_SIZE)


