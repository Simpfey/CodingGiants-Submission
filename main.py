import random, os

# Inicjowanie Funkcji Main
class Main():
    def __init__(self) -> None:
        # Inicjowanie Podstawowych Zmiennych
        self.colors: list = ["♥", "♦", "♣", "♠"]
        self.numbers: list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.fixedNumbers: list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K"]
        self.possiblePositions: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

        self.redColor = ["♥", "♦"]
        self.blackColor = ["♣", "♠"]

        self.cards: list = []

        self.Deck1: list = []
        self.Deck2: list = []
        self.Deck3: list = []
        self.Deck4: list = []
        self.Deck5: list = []
        self.Deck6: list = []
        self.Deck7: list = []

        self.Deck1VisibleCards: int = 1
        self.Deck2VisibleCards: int = 1
        self.Deck3VisibleCards: int = 1
        self.Deck4VisibleCards: int = 1
        self.Deck5VisibleCards: int = 1
        self.Deck6VisibleCards: int = 1
        self.Deck7VisibleCards: int = 1

        self.HoldingDeck: list = []

        self.FinishedHeart: list = []
        self.FinishedDiamond: list = []
        self.FinishedClub: list = []
        self.FinishedSpade: list = []

        # Tworzenie List Do Ułatwienia Dostępu do list

        self.Decks = [self.Deck1, self.Deck2, self.Deck3, self.Deck4, self.Deck5, self.Deck6, self.Deck7]
        self.DecksVisibleCards = [self.Deck1VisibleCards, self.Deck2VisibleCards, self.Deck3VisibleCards, self.Deck4VisibleCards, self.Deck5VisibleCards, self.Deck6VisibleCards, self.Deck7VisibleCards]
        self.FinishedDecks = [self.FinishedHeart, self.FinishedDiamond, self.FinishedClub, self.FinishedSpade]

        self.listPositions = [self.cards,
                              self.HoldingDeck, self.FinishedHeart,self.FinishedDiamond, self.FinishedClub, self.FinishedSpade,
                              self.Deck1, self.Deck2, self.Deck3, self.Deck4, self.Deck5, self.Deck6, self.Deck7]

    # Czyszczenie Konsoli
    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    # Dodawanie Kart do talii Randomowo
    def addCardtoDeck(self, deck, amount) -> list:
        for i in range(amount):
            _ = self.cards[random.randint(0, len(self.cards) - 1)]
            deck.append(_)
            self.cards.remove(_)

        return deck
    
    # Pobieranie Ostatniej Karty Z Talii, A jak nie istnieje oddaje zmeinną "empty"
    def getLastCardFromDeckIfExists(self, deck, empty):
        if len(deck) == 0:
            return empty
        else:
            return deck[-1]
        
    # Rysowanie Talii Kart
    def DrawDeckCards(self):
        for i in range(7):
            for j in range(len(self.Decks[i])):
                if self.Decks[i].index(self.Decks[i][j]) < len(self.Decks[i]) - self.DecksVisibleCards[i]:
                    print("#", end=" ")
                else:
                    print(f"{self.Decks[i][j]}", end=" ")
            
            print("")
        
    # Sprawdzanie czy jest mozliwe wykonanie ruchu
    def validMove(self, num1, num2):
        # Nie można ruszać/dodawać kart z rezerwy kart
        if num2 == 1 or num2 == num1:
            print("Invalid Move!")
            print("Press Any key to continue...")
            input()
        
        # Sprawdzanie czy wsadzamy do ukończonej talii
        elif num2 > 2 and num2 < 7:

            # Sprawdzanie czy karta jest tego samego koloru
            if self.listPositions[num1][-1][0] == self.colors[num2 - 2]:

                # Sprawdzanie czy ukończona talia jest pusta, jak tak to sprawdzamy czy karta to AS
                if len(self.listPositions[num2]) == 0 and self.listPositions[num1][-1][1] == "A":
                    
                    self.listPositions[num2].append(self.listPositions[num1][-1])
                    self.listPositions[num1].remove(self.listPositions[num1][-1])

                # Jak ukończona talia jest pusta, ale karta to nie AS to ruch jest nieprawidłowy
                elif len(self.listPositions[num2]) == 0 and self.listPositions[num1][-1][1] != "A":
                    
                    print("Invalid Move!")
                    print("Press Any key to continue...")
                    input()
                
                # Jak ukończona talia jest niepusta to sprawdzamy czy karta jest kolejna po ostatniej
                else:
                    _ = self.colors.index(self.listPositions[num2 - 2][-1][1])

                    # Sprawdzamy czy karta jest kolejna
                    if self.listPositions[num1][-1][1] == self.fixedNumbers[_ + 1]:

                        self.listPositions[num2].append(self.listPositions[num1][-1])
                        self.listPositions[num1].remove(self.listPositions[num1][-1])

                    else:

                        print("Invalid Move!")
                        print("Press Any key to continue...")
                        input()

            else:

                print("Invalid Move!")
                print("Press Any key to continue...")                
                input()

        # Sprawdzanie czy wsadzamy do talii
        else:
            # "Wyciągamy"/Sprwadzamy informacje karty
            card1 = self.listPositions[num1][-1]
            card2 = self.listPositions[num2][-1]

            # Sprawdzamy czy karty mają kolor na przemian
            if (card1[0] in self.redColor and card2[0] in self.blackColor) or (card1[0] in self.blackColor and card2[0] in self.redColor):

                # Sprawdzamy numer Kart
                card1Number = self.fixedNumbers.index(card1[1])
                card2Number = self.fixedNumbers.index(card2[1])

                    # Sprawdzamy czy numer karty jest kolejny
                if card1Number == card2Number - 1:
                    self.listPositions[num2].append(self.listPositions[num1][-1])
                    self.listPositions[num1].remove(self.listPositions[num1][-1])

                    # Dodajemy do listy widocznej, aby poprzednia karta też była widoczna

                    self.DecksVisibleCards[num2 - 6] += 1

                    if self.DecksVisibleCards[num1 - 6] - 1 > 0 and num1 > 6:
                        self.DecksVisibleCards[num1 - 6] -= 1
                else:
                    print("Invalid Move!")
                    print("Press Any key to continue...")
                    input()
            else:
                print("Invalid Move!")
                print("Press Any key to continue...")
                input()
        
    # Wykonanie ruchu
    def makeaMove(self, num):
        # Ruch z rezerwy
        if num == 1:

            # Sprawdzamy czy rezerwa jest pusta a jak tak to szuflujemy
            if len(self.cards) == 0:
                random.shuffle(self.HoldingDeck)
                self.cards = self.HoldingDeck
                self.HoldingDeck = []
            # W przeciwnym razie dodajemy do kartę "ręki"
            else:
                self.HoldingDeck.append(self.cards[-1])
                self.cards.remove(self.cards[-1])
        else:

            if len(self.listPositions[num - 1]) == 0:
                print("Invalid Move!")
                print("Press Any key to continue...")
                input()

            else:
                try:
                    # Wybieramy 2 karty z talii / pozycję
                    nextMove = int(input("Gdzie Położyć Kartę?: ").split(" ")[0])
                    self.validMove(num - 1, nextMove - 1)
                except ValueError as e:
                    print(e)
                    print("Invalid Move!")
                    print("Press Any key to continue...")
                    input()
    
    # Rysujemy planszę
    def Draw(self) -> None:

        print(self.getLastCardFromDeckIfExists(self.cards, "[]"), end=" ")

        print(self.getLastCardFromDeckIfExists(self.HoldingDeck, "[]"), end=" ")

        # Rysujemy ukończone talie używając wcześniej zdefiniowanej funkcji
        for i in range(len(self.FinishedDecks)):
            print(self.getLastCardFromDeckIfExists(self.FinishedDecks[i], f"[{self.colors[i]}]"), end=" ")

        print("\n")

        self.DrawDeckCards()

    def Win(self) -> None:
        self.clear()
        print("You Win!")
        print("Press Any key to continue...")
        input()
        self.start()

    # Start klasy Main / Gry
    def start(self) -> None:
        self.cards = []
        # Tworzenie kart
        for color in self.colors:
            for number in self.numbers:
                self.cards.append(color + number)

        # Szuflowanie Kart
        random.shuffle(self.cards)

        # Rozdzielanie kart na talie
        for i in range(len(self.Decks)):
            self.addCardtoDeck(self.Decks[i], i + 1 )

        # Game Loop
        while True:
            winCheck = 0
            self.clear()
            for i in self.FinishedDecks:
                if len(i) == 13:
                    winCheck += 1
            if winCheck == 4:
                self.Win()
            self.Draw()

            # Komendy
            cmd = input("\n>> ").split(" ")

            if cmd[0] == "quit" or cmd[0] == "exit":
                break

            elif cmd[0] in self.possiblePositions:
                self.makeaMove(int(cmd[0]))

            else:
                print("Invalid Command")
                print("Press Any key to continue...")
                input()

# Main
if __name__ == "__main__":
    main = Main()
    main.start()