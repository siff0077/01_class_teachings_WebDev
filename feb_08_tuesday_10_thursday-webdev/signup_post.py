from bottle import post, request, redirect
import g
import uuid

@post("/signup")
def _():
  # VALIDATE


  user_id = str(uuid.uuid4())
  user_firstname = request.forms.get("user_firstname")
  user_lastname = request.forms.get("user_lastname")
  user_email = request.forms.get("user_email")
  user_password = request.forms.get("user_password")
  user = {"id":user_id, "email":user_email, "name":user_firstname, "lastname":user_lastname, "password":user_password}
  g.USERS.append(user)
  print(g.USERS)
  return redirect(f"/signup-ok?user-email={user_email}&user-firstname={user_firstname}&user-lastname={user_lastname}&user-password={user_password}")

