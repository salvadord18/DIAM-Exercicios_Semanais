from django.contrib.auth.models import User

new




def criar_users():
    for nome in new_users:
        email = nome + "@iscte.pt"
        password = "12345"
        User.objects.create_user(nome, email, password)