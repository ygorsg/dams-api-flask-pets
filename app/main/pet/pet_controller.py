from flask_restx import Resource, Namespace, fields, abort
from flask import request
from app.main.pet.pet_service import PetService

api = Namespace('pet', description='Manutenção de dados de pets')

# modelo de validação
pet_modelo = api.model('PetModel', {
    'nome': fields.String(required=True, description='Nome do pet'),
    'tipo': fields.String(required=True, description='Tipo do pet (ex: Cachorro, Gato)'),
    'idade': fields.Integer(required=True, description='Idade do pet')
})

@api.route('/')
class PetListResource(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        """Lista todos os pets"""
        return PetService.obter_todos(), 200

    @api.expect(pet_modelo, validate=True)
    @api.response(201, "Pet adicionado com sucesso")
    def post(self):
        """Adiciona um novo pet"""
        try:
            return PetService.adicionar(request.json), 201
        except ValueError as e:
            abort(400, str(e))

@api.route('/<int:id>')
class PetResource(Resource):
    @api.response(200, "Busca realizada com sucesso")
    @api.response(404, "Pet não encontrado")
    def get(self, id):
        """Busca um pet pelo ID"""
        try:
            return PetService.obter_por_id(id), 200
        except ValueError as e:
            abort(404, str(e))

    @api.expect(pet_modelo, validate=True)
    @api.response(200, "Pet atualizado com sucesso")
    @api.response(404, "Pet não encontrado")
    def put(self, id):
        """Atualiza um pet pelo ID"""
        try:
            return PetService.atualizar(id, request.json), 200
        except ValueError as e:
            abort(404, str(e))

    @api.response(204, "Pet removido com sucesso")
    @api.response(404, "Pet não encontrado")
    def delete(self, id):
        """Remove um pet pelo ID"""
        try:
            PetService.remover(id)
            return '', 204
        except ValueError as e:
            abort(404, str(e))
