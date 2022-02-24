from bottle import get, run, static_file, view


#dictionary
person = {"id":"1", "name":"Siff"}

##############################

@get("/person/<person_id>")
def _(person_id):
    # person["last_name"] = "Leva Jensen"
    return person_id

##############################

@get("/app.css")
def _():
    return static_file("/app.css", root=".")

##############################

@get("/")
@view("index")
def show_index_page():
    return 
    
##############################

@get("/items")
@view("items")
def _():
    letters = ["a", "c", "x"]
    # ternary
    return "yes" if "x" in letters else "no"

    # letters.append("d")
    # # print(type(letters))
    # print( dir(letters) )
    # is_b_in_list = "no"
    # if "b" in letters:
    #     is_b_in_list = "yes"
    # return is_b_in_list

    # letters = ["a", "b", "c"]
    # print("#"*30)
    # print(letters)
    # return letters 

##############################

@get("/item")
def show_item():
    name = "Siff" # string - text
    year = 2022 # integer
    return f"Hi {name}, the year is {year}" # f string
    # return "Hi " + name + ", it is" + str(year)
    # return str(year) # type-cast or cast (convert number to string or reversed)

##############################

# port from 0 to 65535
#reserved from 0 to 1024 

run( host="127.0.0.1", port=3333, debug=True, reloader=True )

