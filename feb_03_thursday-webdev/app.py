from bottle import run, get, response, request, post, delete
import json
import uuid 
import re

items = [
    {"id":"1", "name":"a"},
    {"id":"2", "name":"b"},
    {"id":"3", "name":"c"}
]

##############################

# decorator
@get("/")
def _():
    return "Home"

##############################

@get("/items")
def _():
    return json.dumps(items)
    # return str(items)


##############################

@get("/items/<item_id>")
def _(item_id):

    #VALIDATION
    if not item_id:
        response.status = 400
        return "item_id is missing"

    for item in items:
        if item["id"] == item_id:
            return item

    response.status = 400
    return "Item not found"

##############################

#Query strings - very flexible and dynamic
#Every other variable after the 1st starts with &
#127.0.0.1:4444/test?id=1 - params er alt efter ? i url
#                         - request er hele url'en

#EXERCISE: from postman pass following variables to the server via query string (year, school-name, age)
#The server will reply with: 
# "Hi, you are at KEA. The year is 2022 and you are 20 years old"

@get("/exercise")
def _():
    year = request.params.get("year")
    school_name = request.params.get("school-name")
    age = request.params.get("age")
    return f"Hi, your are at {school_name}. The year is {year} and you are {age} years old"

##############################

@get("/test")
def _():

    #REGEX
    #regex - works with any programing language

    user_name = "Siff"
    if not re.match("^[a-zA-Z]*$", user_name):
        return "not a valid name"
    return "congrats, valid name"

    # * makes it possible for the regex to read any number of characters

    # user_phone = "02345678"
    # if not re.match("^[1-9][0-9]{7}$", user_phone): #true or false
    #     return "not a valid phonenumber"
    # return "congrats, valid phonenumber"

##############################

#Friendly URL's - limited by the back-end, not as dynamic as a query-string URL
#127.0.0.1:4444/friendly/brand/xxx/color/xxx

@get("/friendly/brand/<brand_name>/color/<item_color>")
def _(brand_name, item_color):
    return f"You want {brand_name}, and the color is {item_color}"

##############################

@post("/items")
def _():

    # VALIDATION
    if not request.forms.get("item_name"):
        response.status = 400
        return "item_name is missing"
    if len(request.forms.get("item_name")) < 2:
        response.status = 400
        return "item_name must be at least 2 characters long"
    if len(request.forms.get("item_name")) > 20:
        response.status = 400
        return "item_name must be less than 20 characters long"

    item_id = str( uuid.uuid4() )
    item_name = request.forms.get("item_name")
    item_price = request.forms.get("item_price")
    item = {"id":item_id, "name":item_name, "price":item_price}
    items.append(item)

    # print("#"*30)
    # print( type(item_id) )
    return item_id

    # user_firstname = request.forms.get("firstname")
    # user_lastname = request.forms.get("lastname")
    # return f"Hi {user_firstname} {user_lastname}"

##############################

@delete("/items/<item_id>")
def _(item_id):

    # VALIDATION
    # for item in items:

    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            return "Item deleted"

    # IF ITEM NOT FOUND

    return "Item not found"

##############################

#KWARGS
# port 0 to 65635
# port 0 to 1024 are reserved

run(host="127.0.0.1", port=4444, debug=True, reloader=True)