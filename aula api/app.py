from flask import Flask
from flask_restx import Api, Resource, fields 

app = Flask(__name__)

api = Api (
    app,
    version ='1.0',
    title = 'Minha API',
    description = 'API Rest feita com Flask',
    doc='/swagger'
)

ns = api.namespace('usuarios', description='Operações relacionadas a usuarios')

usuario_model = api.model('Usuario',{
    "id": fields.Integer(readonly=True, description='ID do usuario'),
    "nome": fields.String(required=True, description='Nome do usuario')
})

usuarios = [
    {"id":1, "nome": "João"},
    {"id":2, "nome": "Vitor"}
]

@ns.route("/")
class UsuariosList(Resource):
    @ns.doc('Listar todos os usuarios')
    def get(self):
        """Listar todos os usuarios"""
        return usuarios, 200

    @ns.expect(usuario_model)
    @ns.doc('Criar um novo usuario')
    def post(self):
        """Criar um novo usuario"""
        novo_usuario = api.payload
        novo_usuario["id"] = len(usuarios) +1
        usuarios.append(novo_usuario)
        return novo_usuario, 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)