from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario

# # criar banco de dados:
# with app.app_context():
#     database.create_all()

# # criar um usuario:
# with app.app_context():
#     usuario = Usuario(username='Lira', email='lira@gmail.com', senha='123456')
#     usuario2 = Usuario(username='Joao', email='joao@gmail.com', senha='123456')
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()
# #
# fazer busca no banco de dados
with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios[2].email)
