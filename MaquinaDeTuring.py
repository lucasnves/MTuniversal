import sys
from tkinter import E

class MaquinaTuring:

	def LendoArquivo(self):

		# Digite no 'C:...' o diretório aonde está o arquivo que deseja ler com os estados e transições.
		with open(r'C:\Users\Lucas\Área de Trabalho\MaquinaDeTuring\ex3.txt') as arquivo:
			self.transicoes= {}
			for linha in arquivo:
				lendo= linha.split();
				self.transicoes[(lendo[0], lendo[1])]= (lendo[2], lendo[3], lendo[4])
		arquivo.close()

	def infos(self):

		inicial= input("\nDigite o estado inicial: ")
		final= input("Digite o estado final: ")

		self.inicial= inicial
		self.final= final

		self.aceita= "\nAceita! \n"
		self.rejeita= "\nRejeitada! \n"

	def Entrada(self, palavra):
		fita= "B"+ palavra + "B"
		self.fita= list(fita)

	def mostrarFita(self):
		imprimindo= ""

		for string in self.fita:
			imprimindo += string

		print(imprimindo)

	def maquina(self):
		pos=0
		i=0
		Eatual= self.inicial
		ESTADOS= list(self.transicoes)

		while True:
			try:
				if ESTADOS.count((Eatual, self.fita[pos]))==1:
					reposic= self.transicoes[(Eatual, self.fita[pos])]

					i+=1
					print("\nINT: %d" % i + "º - \n" + "Estado: (" + Eatual + "), Foi para: (" + reposic[0] + "), Leu: '" + self.fita[pos] 
					+ "', Escreveu: '" + reposic[1] + "', Moveu para: " + reposic[2] +"\n")

					Eatual= reposic[0]
					self.fita[pos]= reposic[1]

					if reposic[2]=="L": pos -= 1
					else: pos += 1
					
					self.mostrarFita()

				else:
					break
			except:
				print("\nPalavra não aceitavel\n")
				break;

		print(self.aceita) if self.final.count(Eatual)==1 else print(self.rejeita)



MT= MaquinaTuring()
MT.LendoArquivo()
MT.infos()
dnv="S"

while (dnv=="S"):
	palavra= input("Digite a palavra desejada: ")
	MT.Entrada(palavra)
	MT.maquina()
	dnv= input("Tentat outra palavra? [S | N]: ")
