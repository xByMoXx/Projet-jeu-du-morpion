import random

class jeu():

    def self(self):
        self.player1 = 'X'
        self.player2 = 'O'
        self.round = 'X'
        self.number_of_rounds = 0
        self.plateau = [[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']]

    def debut(self):
        """Choix du joueur"""
        self.player1 = input((print('Chose your symbol. X / O (1/2)'))) 
        if self.player1 == 1:
            self.player1 = 'X'
            self.player2 = 'O'
        else:
            self.player1 = 'O'
            self.player2 = 'X'

    def tirage_au_sort(self):
        self.round = random.choice(1, 2)

    def affichage_plateau(self):
        print(self.plateau[0][0] + " | " + self.plateau[0][1] + " | " + self.plateau[0][2])
        print("---|---|---")
        print(self.plateau[1][0] + " | " + self.plateau[1][1] + " | " + self.plateau[1][2])
        print("---|---|---")
        print(self.plateau[2][0] + " | " + self.plateau[2][1] + " | " + self.plateau[2][2])

    def tour_de_jeu(self):
        print("It's the turn of the " + self.round + " player." )
        choosed_box = input(int("Choose a box (1-9)"))
        if choosed_box <= 3:
            if self.plateau[0][choosed_box - 1] == ' ':
                self.plateau[0][choosed_box - 1] = self.round
            else:
                print("This box is already occupied.")
                main.game.tour_de_jeu()
        
        elif choosed_box <= 6:
            if self.plateau[1][choosed_box - 1] == ' ':
                self.plateau[1][choosed_box - 1] = self.round
            else:
                print("This box is already occupied.")
                main().game.tour_de_jeu()
        
        elif choosed_box <= 9:
            if self.plateau[2][choosed_box - 1] == ' ':
                self.plateau[2][choosed_box - 1] = self.round
            else:
                print("This box is already occupied.")
                main().game.tour_de_jeu()

        self.number_of_rounds += 1


def main():
    game = jeu()
    game.debut()
    game.tirage_au_sort()
    while game.self().number_of_rounds < 9:
        game.tour_de_jeu()
        

'''On lance le jeu'''
main()



'''class player():
    
    def self(self):
        self.player = jeu.debut(self)'''
