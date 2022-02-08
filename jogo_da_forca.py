##JOGO DA FORCA
from random import choice
import platform
import os

#global
TEMAS = {

	'programacao': [
					"python",
					"java",
					"javascript",
					"html",
					"css"
					],
	'veiculos'   : [
					"moto"
					"carro",
					"bicicleta",
					"aviao"],
	'comidas'	: [
					"arroz",
					"feijao",
					"macarrao",
					"carne",
					"peixe"],
	#'anime': [],
	
}


class Game:
	
	def __init__(self):
		
		self.forca = 7
		
		#pegar um tema aleatorio
		self.tip = choice(list(TEMAS))
		
		#pegar uma palavra aleatoria desse tema
		self.words = TEMAS[self.tip]
		
		self._correct_word = None
	
	def start(self):
		
		#selecionando a palavra para 
		word = choice(self.words)
		
		#salvando a palavra selecionada
		self._correct_word = word
		
		#usando o metodo privado para enconder as letras
		hidden_word = self._hide_letters(word)
		
		#inicia o loop do jogo
		self.render(hidden_word)
		
	
		
			
	def render(self,hidden_word):
		"""
		metodo de renderização (loop do jogo)
		
		esse metodo não para enquanto o jogador
		não ganhar ou perder.
		
		
		variavel de estado armazena uma lista
		formada pelo metodo privado _hide_letters,
		contendo o a forma traçada e a forma original
		da palavra correta.
		
		Baseado nas entradas do jogador, esse metodo
		é o responsavel pelo tratamento de todo o estado
		do jogo, desde o inicio ao fim, subtraindo as
		vidas, mostrando os traçados, checando se o
		as letra foi encontrada e se o jogador ainda tem
		vidas.
		
		
		"""
		
		
		#variavel local
		state = hidden_word # [trace, word]
		
		#armazena as letras que o usuario ja usou.
		previous_letters = [] 
		
		while self.forca != 0:
			
			#Limpando a tela
			#Tratamento para que o jogo limpe a tela
			#no Windows e no Linux
			if platform.system() == "Windows":
				os.system("cls")
			
			else:
				os.system("clear")
			
			
			# PARTE VISUAL
			
			
			#Indica para o usuario a dica
			print("DICA : " + self.tip)
			
			
			#vidas
			print("chances : ",end="")
			print(" ♥ "*self.forca,end="")
			
			print("\n") 
			
			#letras já usadas
			print("letras que já foram usadas => ", end=" ")
			for letter in previous_letters:
				print(letter, end=" ")
			
			print()
			
			
			#renderizando os traços
			for word in state[0]:
				
				print(word, end=" ")
				
			
			print("\n") 
			
			#entrada do usuario
			user_choice = input("selecione uma letra: ")
			
			
			#tratando se não for uma letra (char)
			if len(user_choice.lower()) > 1:
				print("Por favor, digite uma palavra por vez!")
				input("Enter para continuar...")
				continue
				
			#tratando se é uma letra
			if not user_choice.isalpha():
				input("Por favor digite apenas letras!")
				continue
				
				
			
			#Em caso de ser uma letra
			if user_choice in state[1]:
				
				print("Você encontrou uma letra!")
				
				#modificando o estado
				for index,letter in enumerate(state[1]):
					
					if letter == user_choice:
						state[0][index] = letter
			
			#checa se a letra que o usuario escolheu ja foi usada
			elif user_choice in previous_letters:
				
				print("Você ja usou essa letra!")
				input("Enter para continuar...")
				
			#caso a letra não esteja na palavra!
			else:
				
				print("você errou!")
				
				previous_letters.append(user_choice)
				
				self.forca -= 1
				
				input("Enter para continuar...")
				
			
			#checando o estado das traços
			if not "_" in state[0]: break
					
				
				
				
		
		if self.forca > 0:
			print("parabens você venceu!!")
			
			print(" A palavra é " + self._correct_word.upper())
			
		else:
			
			print("não foi dessa vez!")
			
			print(" A palavra era " + self._correct_word.upper())
						
					
			
			
		
	
	def _hide_letters(self,word):
		"""
		Metodo que ofusca a letra selecionada pelo
		metodo self.start:
			
		
		retorno
		|	uma lista com duas listas dentro
		|	que contem as letras da palavra em traços e
		|	na forma original.
		|
		1° - lista da forma traçada da palavra.
		2° - lista da forma original da palavra.
		"""
		
		trace, letters = [], []
		
		#transforma cada letra da palavra em traços
		#e quebra em pedaços armazenado em letters
		for l in word:
			
			trace.append("_")
			letters.append(l)
			
		
		return [trace,word] 
		
	
	
		
		


def main():
	#instancia do jogo
	game = Game()
	
	#iniciando o jogo
	game.start()
	
	
	
if __name__ == "__main__":
	main()