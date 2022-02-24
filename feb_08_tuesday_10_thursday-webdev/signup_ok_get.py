
from bottle import get, request, view
import g

# query string expected with user-email
@get("/signup-ok") 
@view("signup-ok")
def _():
  user_email = request.params.get("user-email")
  user_firstname = request.params.get("user-firstname")
  user_lastname = request.params.get("user-lastname")
  user_password = request.forms.get("user_password")
  return dict(user_email=user_email, user_firstname=user_firstname, user_lastname=user_lastname, user_password=user_password)