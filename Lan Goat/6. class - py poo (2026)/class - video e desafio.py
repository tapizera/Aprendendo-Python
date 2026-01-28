# criando uma class e seus atributos
class Canal:
    #as 'funcoes' dentro das class na vdd são metodos
    # init é o método base que starta quando a class é chamada
    def __init__(self, nome, descricao, incritos):
        self.nome = nome
        self.descricao = descricao
        self.incritos = incritos
        self.videos = []
        #self.playlists = [[self.videos]]
        # self.playlists:list[Playlist] = [] #tipado
        self.playlists = []

    #definindo o metodo increver-se
    def inscrever(self, quantidade=1):
        self.incritos =+ 1

    #adionando video na lista de videos
    def postar(self, video):
        #se o video já existir entao nao posta
        if video in self.videos:
            print('Esse vídeo já existe')
            return
        self.videos.append(video)

    # def info(self):
    #    print(self.playlists)

    def info_playlists(self):
        for playlist in self.playlists:
            print(f'Playlist: {playlist.nome}')
            playlist.info_videos()

    def add_playlists(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print('já tá')

    def remove_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print('nao tem essa playlist')

# criando outra classe mas que herda da classe 'Canal'

class Canal_Empresarial(Canal):
    def __init__(self, nome, descricao, incritos):
        super().__init__(nome, descricao, incritos)
        # o _ indica q é privado dessa class
        self._equipe = []
        self._titulo = ''
    
    @property
    def equipe(self):
        return self._equipe
    

class Video:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.vizualiacoes = 0
        self.likes = 0
        self.deslikes = 0
        self.comentarios = []

    def __repr__(self):
        return f'{self.titulo}'
    
    def assistir(self):
        self.vizualiacoes += 1 

    def gostei(self):
        self.gostei += 1

    def nao_gostei(self):
        self.nao_gostei += 1

    def inscrever(self):
        self.inscrever += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)
    
    def info(self):
        print(f'Título: {self.titulo}')
        print(f'Descrição: {self.descricao}')
        print(f'{self.likes} Likes')
        print(f'{self.deslikes} Deslikes')
        if self.comentarios in self.comentarios:
            print('Comentários:')
            print(f'{self.comentarios}\n')
        else:
            print('Comentários:')
            print('(Ainda não há comentários)\n')
        

# Desafio

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.videos = []
        #self.videos:list[Videos] = [] #tipado
    
    def add_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print('esse já tá na playlist')

    def remover_video(self, video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print('o video nao tá na playlist')
    '''
    #errado
    def info(self):
        print(self.videos)
    ''' 
    def info_videos(self):
        for video in self.videos:
            video.info()

# No terminal:

# criando videos
video_poo = Video('Python objetos', 'Aprenda agora')
video_andreyoung = Video('AndreYoung vs todas as pessoas', 'baixe meu jogo 9kings')

# criando playlists com videos
playlist_andrezitos = Playlist(video_andreyoung)
playlist_andrezitos.add_video(video_andreyoung)

playlist_langoat = Playlist(video_poo)
playlist_langoat.add_video(video_poo)

# criando canais com playlists
canal_do_andre = Canal('Andrezitos', 'baixe 9kings', 955000)
canal_do_andre.add_playlists(playlist_andrezitos)

canal_do_lan = Canal('Lan Code', 'gatos de programa', 43000)
canal_do_lan.add_playlists(playlist_langoat)

# postando video no canal
canal_do_lan.postar(video_poo)
canal_do_andre.postar(video_andreyoung)

# exibindo a playlist
canal_do_lan.info_playlists()