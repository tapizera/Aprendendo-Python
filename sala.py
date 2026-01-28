class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'esse tal de {self.nome} tem {self.idade} anos'

print(Pessoa('joazin', 17))

class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie
    def __str__(self):
        return f'esse tal de {self.nome} tem {self.idade} anos e está no {self.serie}° ano'
    
print(Aluno('nome', 20, 3))

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
    def __str__(self):
        return f'esse tal de {self.nome} tem {self.idade} anos e trabalha de {self.cargo}'
    
# print(Funcionario('jucicreudo', 22, 'mecanico'))

class Sala:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def __str__(self):
        return f' > nome da sala: {self.nome}\n > alunos da sala: {', '.join(self.alunos)}\n > N° de alunos: {len(self.alunos)}'
    
nome_da_sala = input('qual o nome da sala?: ')
sala = Sala(nome_da_sala)
while True:
    quer = input('quer botar aluno da sala?(s/n?): ')
    if quer.lower() == 's':
        nome_do_individuo = input('qual o nome do individuo?: ')
        sala.adicionar_aluno(nome_do_individuo)
    else:
        break

print(sala) 