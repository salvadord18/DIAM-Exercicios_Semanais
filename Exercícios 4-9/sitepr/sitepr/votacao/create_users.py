from django.contrib.auth.models import User

def criar_users():
    password = "pass"
    u = User.objects.create_user(name, mail, password)
    aluno = Aluno(user=u, curso="IGE")
    aluno.save()