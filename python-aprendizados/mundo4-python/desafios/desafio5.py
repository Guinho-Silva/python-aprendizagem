"""
5)Crie uma classe gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.Crie também um método que permita mostrar a ficha desse gamer"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from rich.text import Text

console = Console()
class Gamer:
    def __init__(self, nome, nick)-> str:
        self.nome = nome

        self.nick = nick

        self.jogos_favoritos = []
    

    def JogosFavoritos(self,*jogo_digitado)-> str:

        for jogos in jogo_digitado:
            if isinstance(jogos, (list, tuple)):
                self.jogos_favoritos.extend(jogos)
            else:
                self.jogos_favoritos.append(jogos)

    def Mostrarjogos(self):
        return self.jogos_favoritos
    

    def fich(self):
       
       tabela = Table(title="Ficha do Jogador")

       tabela.add_column("Campo", style="cyan")
       tabela.add_column("Info", style="white")

       tabela.add_row("Nome", self.nome)
       tabela.add_row("Nick", self.nick)
       tabela.add_row("Jogos", ", ".join(self.jogos_favoritos))

       console.print(tabela)
# testando a classe

t1 = Gamer('Iago', 'Mandrakinho')

t1.JogosFavoritos('God of War', 'Minecraft')

t1.fich()
