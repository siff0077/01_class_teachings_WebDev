from bottle import post, redirect, request
import g
import re

@post("/login")
def _():
  # VALIDATE
  # FIRST THING: Always check if the vriable was passed in the form
  if not request.forms.get("user_email"):
    return redirect("/login?error=user_email")
  if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect("/login?error=user_email")

  user_password = request.forms.get("user_password")
  user_email = request.forms.get("user_email")
  # FIRST THING: Always check if the vriable was passed in the form
  if not request.forms.get("user_password"):
    return redirect(f"/login?error=user_password&user-email={user_email}")
  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/login?error=user_password&user-email={user_email}")
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/login?error=user_password&user-email={user_email}")

  for user in g.USERS:
    if request.forms.get("user_email") == user["email"] and request.forms.get("user_password") == user["password"]:
      return redirect("/admin")
      # SUCCESS

  return redirect("/login?error=unknown_user_information")
  