class Pet:
    pets = [
        {'nome': 'Rex', 'tipo': 'Cachorro', 'idade': 5, 'id': 1},
        {'nome': 'Mimi', 'tipo': 'Gato', 'idade': 3, 'id': 2},
        {'nome': 'Lola', 'tipo': 'Cachorro', 'idade': 4, 'id': 3},
        {'nome': 'Nina', 'tipo': 'Papagaio', 'idade': 11, 'id': 4},
        {'nome': 'Fido', 'tipo': 'Cachorro', 'idade': 13, 'id': 5},
        {'nome': 'Sia', 'tipo': 'Gato', 'idade': 7, 'id': 6},
        {'nome': 'Jerônimo', 'tipo': 'Peixe', 'idade': 3, 'id': 7},
        {'nome': 'Burrito', 'tipo': 'Aranha', 'idade': 2, 'id': 8},
        {'nome': 'Bella', 'tipo': 'Gato', 'idade': 9, 'id': 9},
        {'nome': 'Max', 'tipo': 'Cachorro', 'idade': 4, 'id': 10}
    ]

    @classmethod
    def adicionar(cls, pet):
        """Adiciona um novo pet"""
        pet['id'] = cls._gerar_novo_id()
        cls.pets.append(pet)
        return pet

    @classmethod
    def obter(cls, id=None):
        """Obtém todos os pets ou um pet específico pelo ID"""
        if id:
            return next((pet for pet in cls.pets if pet['id'] == id), None)
        return cls.pets

    @classmethod
    def remover(cls, id):
        """Remove um pet pelo ID"""
        pet = cls.obter(id)
        if pet:
            cls.pets = [p for p in cls.pets if p['id'] != id]
            return {"mensagem": f"Pet com ID {id} removido com sucesso"}
        return {"erro": f"Pet com ID {id} não encontrado"}

    @classmethod
    def alterar(cls, id, novo_pet):
        """Atualiza os dados de um pet pelo ID"""
        pet = cls.obter(id)
        if not pet:
            return {"erro": "Pet não encontrado"}

        index = cls.pets.index(pet)
        pet.update({k: v for k, v in novo_pet.items() if v is not None})
        cls.pets[index] = pet
        return pet

    @classmethod
    def _gerar_novo_id(cls):
        """Gera um novo ID único"""
        if not cls.pets:
            return 1
        return max(pet['id'] for pet in cls.pets) + 1
