from bottle import get, request, view

# Query string will be used in this route
# Eg. /login?error=user_email
# Eg. /login?error=user_password
@get("/login")
@view("login")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user-email")
  return dict(error=error, user_email=user_email)