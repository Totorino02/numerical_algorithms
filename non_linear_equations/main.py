from utils import getFunction, balayage, is_number

from bissection import bissection
from secante import secante
from newton import newton
from pointFixes import fixed_points


def execute_functions(f, g, a, b, x0):
	if f:
		print("\n\nNEWTON : ", newton(f, x0))

		bissectionResults = []
		secanteResults = []
		for interval in balayage(f, a, b):
			c, d = interval

			bissectionResults.append(bissection(f, c, d))
			secanteResults.append(secante(f, c, d))
			
		if bissectionResults:
			print("\nDICHOTOMIE : ", *bissectionResults, sep="\t")
		else:
			print("\nDICHOTOMIE : Aucun resultat")

		if secanteResults:
			print("\nCORDE : ", *secanteResults, sep="\t")
		else:
			print("\nCORDE : Aucun resultat")

	if g:
		print("\nPOINTS FIXES : ", fixed_points(g, x0))


def main():	
	print("""


        RESOLUTION D'EQUATIONS DE LA FORME f(x) = 0


        Ce programme présente les quatre méthodes suivantes:
            - méthode de la dichotomie
            - méthode de NEWTON
            - méthode de la corde
            - méthode des points fixes


        # Conditions d'utilisation du programme : 
            - la fonction principale est f(x)
            - la fonction secondaire qui sera utilisée pour la méthode 
                des points fixes est g(x)
            - la seule variable autorisée dans les fonctions est << x >>
            - x0, a et b sont des nombres réels
            - la précision epsilon doit être inférieur à 10e-4       

            - n'entrez aucune valeur qui ne respecte pas ces règles

        
        # Comment entrer des fonction : 
            - la multiplication dit être explicite : 2x -> 2 * x
            - cos();  sin
    
    """)
	
	try:

		data_are_correct = False
		max_nb = 4
		ctr = 0

		while data_are_correct == False and ctr < max_nb:
			ctr += 1

			""" #f = lambda x : (x**2 + 1) / (x - 1)
			f = lambda x : x**2 - 1
			g = lambda x : 1 / x
			a = -2
			b = "sd"
			x0 = -3 """

			f = getFunction()
			g = getFunction("Entrez la function : g(x) = ")
			x0 = input("Entrer la valeur de x0 : ")
			a = input("Entrer la valeur de a : ")
			b = input("Entrer la valeur de b : ")
			# precision = float(input("Entrer la valeur de la precision : "))

			user_confirmation = input("Validez-vous les donnees saisies ? (oui/non): ")
			if user_confirmation == "oui":
				if not (is_number(a) and is_number(b) and is_number(x0)):
					print("<a>, <b> et <x0> doivent etre des nombres.")
					x0 = input("Entrer la valeur de x0 : ")
					a = input("Entrer la valeur de a : ")
					b = input("Entrer la valeur de b : ")
				
				if float(a) == float(b):
					if f(a) == 0:
						func_less_solutions = a
					else:
						print("<a> doit etre inferieur a <b>.")
						a = input("Entrer la valeur de a : ")
						b = input("Entrer la valeur de b : ")
				elif a > b:
					print("<a> doit etre inferieur a <b>.")
					a = input("Entrer la valeur de a : ")
					b = input("Entrer la valeur de b : ")

				if is_number(a) and is_number(b) and is_number(x0) and float(a) < float(b):
					a = float(a)
					b = float(b)
					x0 = float(x0)
					data_are_correct = True
					execute_functions(f, g, a, b, x0)
				else:
					print("Les donnees saisies ne sont pas correctes, recommencez depuis le debut.")
					continue

			elif user_confirmation == "non":
				print("Resaisie des donnees")
				continue

			else:
				print("Veuillez respecter les consignes s il vous plait")


	except:
		print("\nImpossible d executer le programme. Veuillez respecter les consignes s il vous plait\n")



if __name__ == "__main__":
    main()
