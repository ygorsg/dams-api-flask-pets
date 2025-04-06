from app.main.pet.pet_db import Pet

class PetService:
    @staticmethod
    def obter_todos():
        """Obtém todos os pets"""
        return Pet.obter()

    @staticmethod
    def obter_por_id(id):
        """Obtém um pet pelo ID"""
        pet = Pet.obter(id)
        if not pet:
            raise ValueError(f"Pet com ID {id} não encontrado")
        return pet

    @staticmethod
    def adicionar(dados):
        """Adiciona um novo pet"""
        # validação adicional, se necessário
        if not dados.get('nome') or not dados.get('tipo') or 'idade' not in dados:
            raise ValueError("Dados inválidos para adicionar um pet")
        return Pet.adicionar(dados)

    @staticmethod
    def atualizar(id, dados):
        """Atualiza um pet pelo ID"""
        pet = Pet.obter(id)
        if not pet:
            raise ValueError(f"Pet com ID {id} não encontrado")
        return Pet.alterar(id, dados)

    @staticmethod
    def remover(id):
        """Remove um pet pelo ID"""
        pet = Pet.obter(id)
        if not pet:
            raise ValueError(f"Pet com ID {id} não encontrado")
        return Pet.remover(id)
