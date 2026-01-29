
print("Hello, World!")

#não lê o código pra relembrar, tá mal explicado e o foco foi em fazer um desafio a si mesmo
#só executa

# --------------------- CRIANDO A CLASSE PESSOA ------------------------

# __init__() 
    # é um método especial (também chamado de "método mágico"). 
    # serve para inicializar os atributos do objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        print(f'\n> nome: {self.nome}\n> idade: {self.idade} anos')

############## NO TERMINAL

print('\n --- NOVA PESSOA --- ')
nomepessoa = input('nome da pessoa: ')
idadepessoa = int(input('idade da pessoa: '))
novapessoa = Pessoa(nomepessoa, idadepessoa)

# foraluno = input(f'{nomepessoa} é aluno? (s/n): ')
# if foraluno.lower().strip() == 's':
#     seriealuno = int(input('q série?: '))
#     #add aluno na sala
#     quiserverinfo2 = input('qier ver a info da pessoa?(s/n): ')
#     if quiserverinfo2.lower().strip() == 's':
#         novapessoa.infoaluno()

quiserverinfo = input('quer ver a info da pessoa? (s/n): ')
if quiserverinfo.lower().strip() in ('s', 'sim'):
    novapessoa.info()   



# ------------- CRIANDO A CLASSE ALUNO HERDANDO DE PESSOA -------------

# super( ) 
    # é uma função embutida do Python 
    # serve p retornar uma referência à superclasse da classe atual.
    # usada para chamar métodos da classe pai, como __init__().

class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie

    def infoaluno(self):
        print(f'\n> nome: {self.nome}\n> idade: {self.idade} anos\n> série: {self.serie}° ano')

    # gpt falou p botar p ficar melhor
    def __str__(self):
        return f'{self.nome} ({self.idade} anos)'
    
    # e isso tmb
    def __repr__(self):
        return f"Aluno(nome={self.nome!r}, idade={self.idade}, serie={self.serie!r})"

############## NO TERMINAL

print('\n --- NOVO ALUNO --- ')
nomealuno = input('nome do aluno: ')
idadealuno = int(input('idade do aluno: '))
serie = input('serie do aluno: ')
novoaluno = Aluno(nomealuno, idadealuno, serie)

quiserverinfodoaluno = input('quer ver a info do aluno? (s/n): ')
if quiserverinfodoaluno.lower().strip() in ('s', 'sim'):
    novoaluno.infoaluno()



# ---------- CRIANDO A CLASSE FUNCIONARIO HERDANDO DE PESSOA -----------

print('\n --- NOVO FUNCIONARIO --- ')
nomefuncionario = input('nome do funcionario: ')
idadefuncionario = int(input('idade do funcionario: '))
cargofuncionario = input('cargo do funcionario: ')

class Funcionario(Pessoa):
        def __init__(self, nome, idade, cargo):
            super().__init__(nome, idade)
            self.cargo = cargo

        def infofunc(self):
            print(f'\n > nome: {self.nome}\n > idade: {self.idade} anos\n > cargo: {self.cargo}')



# ------------- CRIANDO CLASSES HERDANDO DE FUNCIONARIO ---------------

# Criando a classe Professor apenas se  for 'professor' ou 'professora' com ajuda (IA deu help)
if cargofuncionario in ('professor', 'professora', 'prof'):
    class Professor(Funcionario):
        def __init__(self, nome, idade, cargo, materia):
            super().__init__(nome, idade, cargo)
            self.materia = materia

        def infoprof(self):
            print(f'\n> nome: {self.nome}\n> idade: {self.idade}\n> cargo: {self.cargo}\n> materia: {self.materia}')
 
    # Pedindo a matéria e criando o objeto Professor
    materiaprof = input('materia do professor: ')
    novoprofessor = Professor(nomefuncionario, idadefuncionario, cargofuncionario,materiaprof)
    quiserverinfodoprof = input('quer ver a info do professor? (s/n): ')
    if quiserverinfodoprof.lower().strip() in ('s', 'sim'):
        novoprofessor.infoprof()



elif cargofuncionario in ('diretor', 'diretora', 'diret'):
    class Diretor(Funcionario):
        def __init__(self, nome, idade, cargo):
            super().__init__(nome, idade, cargo)

        def infodiretor(self):
            print(f'\n> nome: {self.nome}\n> idade: {self.idade}\n> cargo: {self.cargo}')

    novodiretor = Diretor(nomefuncionario, idadefuncionario, cargofuncionario)
    quiserverinfododiret = input('quer ver a info do diretor? (s/n): ')
    if quiserverinfododiret.lower().strip() in ('s', 'sim'):
        novodiretor.infodiretor()



elif cargofuncionario in ('coordenador', 'cordenadora', 'coord'):
    class Coordenador(Funcionario):
        def __init__(self, nome, idade, cargo):
            super().__init__(nome, idade, cargo)

        def infocoord(self):
            print(f'\n> nome: {self.nome}\n> idade: {self.idade}\n> cargo: {self.cargo}')
        
    novocoordenador = Coordenador(nomefuncionario, idadefuncionario, cargofuncionario)
    quiserverinfodocoord = input('quer ver a info do coordenador? (s/n): ')
    if quiserverinfodocoord.lower().strip() in ('s', 'sim'):
        novocoordenador.infocoord()



else:
    novofuncionario = Funcionario(nomefuncionario, idadefuncionario, cargofuncionario)
    quiserverinfodofunc = input('quer ver a info do funcionario? (s/n): ')
    if quiserverinfodofunc.lower().strip() in ('s', 'sim'):
        novofuncionario.infofunc()



# -------------------- CRIANDO A CLASSE SALA ------------------------

class Sala:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def addaluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
        else:
            raise ValueError("Apenas objetos do tipo Pessoa podem ser adicionados como alunos.")
            # nao pode aluno que nao seja do tipo pessoa ksksks
    
    # ia daq pediu p botar isso
    def qtddealunos(self):
        return len(self.alunos)
    
    def infosala(self):
        print(f'\n> nome da sala: {self.nome}')
        print(f'> alunos ({len(self.alunos)}):')

        for aluno in self.alunos:
            print(f'  - {aluno.nome}, {aluno.idade} anos ({aluno.serie}° ano)')

    # gpt recomendou botar
    def __str__(self):
        return f'Sala {self.nome}'
    
    # gpt tmb
    def __repr__(self):
        return f"Sala(nome={self.nome!r}, alunos={len(self.alunos)})"


print('\n --- NOVA SALA --- ')
nomesala = input('nome da sala: ')
novasala = Sala(nomesala)

quiseraddaluno = input('quer add aquele aluno ou outro? (1/2): ')
if quiseraddaluno.strip() == '1':
    novasala.addaluno(novoaluno)
elif quiseraddaluno.strip() == '2':
    nomealuno2 = input('nome do aluno: ')
    idadealuno2 = int(input('idade no aluno: '))
    serie2 = input('serie do aluno: ')
    novoaluno2 = Aluno(nomealuno2, idadealuno2, serie2)
    novasala.addaluno(novoaluno2)

quiserverinfodasala = input('quer ver a info da sala? (s/n): ')
if quiserverinfodasala.lower().strip() in ('s', 'sim'):
    novasala.infosala()
     
    

# ------------------- CRIANDO A CLASSE ESCOLA  -----------------------

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.salas = []

    def addsala(self, novasala):
        if isinstance(novasala, Sala):
            self.salas.append(novasala)
            # se a sala foi do tipo Sala, pode add
        else:
            raise ValueError("Apenas objetos do tipo Sala podem ser adicionados.")
            # se n for n pode

    # Gpt deu help aqui
    def totaldealunos(self):
        total = 0
        for sala in self.salas:
            total += sala.qtddealunos()
        return total
        
    # aqui tmb
    def listarsalas(self):
        for sala in self.salas:
            print(f'- {sala}')
        
    # e aqui tmb
    def listartudo(self):
        for sala in self.salas:
            print(f'Sala: {sala.nome}')

            if not sala.alunos:
                print('  (sem alunos)')
            # equivalente a:
            #if len(alunos) == 0:
                #print(' (sem alunos)')

            else:
                for aluno in sala.alunos:
                    print(f'  - {aluno.nome} ({aluno.idade} anos)')
    
    # gpt
    def __str__(self):
        return f'Escola {self.nome}'

    # gpt
    def __repr__(self):
        return f"Escola(nome={self.nome!r}, salas={len(self.salas)})"

    # gpt
    def infoescola(self):
        print(f'\n> Nome da escola: {self.nome}')
        print(f'> Salas ({len(self.salas)}):')
        if not self.salas:
            print('\n  (nao tem sala nao)')
            return

        for sala in self.salas:
            print(f'  - {sala.nome}')

        print(f'> Alunos ({self.totaldealunos()}):')
        if not self.salas:
            print('\n(tem sala nao)')
            return

        for sala in self.salas:
            for aluno in sala.alunos:
                print(f'  - {aluno.nome}, {aluno.idade} anos - {aluno.serie}°ano') 
                print(f'    sala: {sala.nome})')

        #self.listartudo()

print('\n --- NOVA ESCOLA --- ')
nomeescola = input('nome da escola: ')
novaescola = Escola(nomeescola)

quiseraddsala = input('quer add aquela sala ou outra? (1/2): ')
if quiseraddsala.strip() == '1':
    novaescola.addsala(novasala)
elif quiseraddsala.strip() == '2':
    nomesala2 = input('nome da sala: ')
    novasala2 = Sala(nomesala2)
    novaescola.addsala(novasala2)

quiserverinfodaescola = input('quer ver info da escola? (s/n): ')
if quiserverinfodasala.lower().strip() in ('s', 'sim'):
    novaescola.infoescola()
