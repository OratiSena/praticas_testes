#teste
def email_valido(email):
  if not email:
    return False
  if "@" not in email or email.count("@") > 1:
    return False

  usuario, dominio = email.split("@", 1)

  return (
      usuario != ""
      and "." in dominio
      and not dominio.startswith(".")
      and not dominio.endswith(".")
  )
