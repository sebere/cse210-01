from random import randint
"*** DICE juego de dados ***"

class Die:
    "en este caso dedo crear la clase generica"

    def __init__ (self):
        "se crea las funciones que contengas los valores y los puentos"
        self.value = 0
        self.points = 0

        """se crea la funciones que crean las funciones de las condiciones del juego 
            es decir, los valores de los dados VALUE y los puntos de los valores POINT
         """

    def roll(self):

        "se buscan los valores aleatores de 1 a 6"
        self.values = randint(1, 6)

        "se crean los valores para crear las condiciones de como ganar los puntos"
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0


""" se inicia una nueva clase donde se desarrollen las condiciones del juego"""

class Director:

    def __init__(self):

        """ contiene las VARIABLES para poder inicar el juego"""
        """ dentro de las clases todo debe contener el SELF. """

        """Este contiene los valores random dentro de una lista"""
        self.dice =[]
        """este es un boleano para saber si el jugador esta guando (si o no) """
        self.is_playing = True
        """este contiene los valores que se van sumando en el turno de juego"""
        self.score = 0
        """este contiene el puntaje total del juego"""
        self.total_score = 0
        """ SE CREAN LAS FUNCIONES DE CADA UNA DE LAS VALIABLES"""

        """se crean el rango para las el juego"""
        for i in range(5):
            die = Die()
            self.dice.append(die)


    def start_game(self):

        """las funciones se ponen dentro de un loop WHILE"""

        while self.is_playing:
            
            """ funcion para saber si se juega o no  Roll dice? [y/n] """
            self.get_inputs()
            """ la sumatoria de los puntos en cada turno"""
            self.do_updates()
            """ los resultados finales del juego"""
            self.do_outputs()
    
    def get_inputs(self):
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")

    def do_updates(self):

        """si el usuario no juega se retorna"""
        if not self.is_playing:
            return

        """" se hace un bucle para revisar todos los elementos de la lista"""

        for i in range(len(self.dice)):
            """se crea una funcion par el conteo del bucle"""
            die = self.dice[i]
            die.roll()
            self.score += die.points
            """fuera delbucle se va llevando la sumatoria general"""
        self.total_score += self.score

    def do_outputs(self):

        """se revisa si el usuario va a jugar"""
        if not self.is_playing:
            return
        """ se crean dos valores el que muestra los valores de los dados
            y la sumatoria de los puntos por los juegos ganados"""

        """se crea primero la valirable que contenga los valores"""
        values = ""

        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.values} "
            
        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)


director = Director()
director.start_game()

        



    



