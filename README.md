## Sposób uruchomienia projektu:

1. `pip install -r requirements.txt`
    Aby zainstalowac wszystkie wymagane biblioteki
2. `python main.py`
    Aby uruchomic program
	
<p>! Pliku nie otwieramy za pomocą innego pliku .py !</p>
np:
```py
import main
```
<p>Kod Wtedy nie zadziała<p>

## Jak grać:

1. Wpisz "quit" lub "exit" aby wyjsc z gry


na początku widać planszę, np.:

```
♦J [] [♥] [♦] [♣] [♠]

♥Q
# ♦6
# # ♠K
# # # ♥A
# # # # ♣2
# # # # # ♣Q
# # # # # # ♥10
```

Ponumerowanie pól w planszy:

```
1 2 3 4 5 6

7
# 8
# # 9
# # # 10
# # # # 11
# # # # # 12
# # # # # # 13
```

<p>Potrzeba wpisać ***dany*** numerek pola aby wejść z nim w interakcję</p>
<p>Gra sama się spyta gdzie postawić daną kartę, bądź uruchomi akcję, 
np: Aby przetasować pustą rezerwę trzeba podać numer pola 1 podczas gdy rezerwa jest pusta</p>
<p>Karty z rezerwy można wsadzać tylko do slotu 2 (aka. "trzymane" karty), dopiero trzymane karty można położyć na końcowe stosy lub talie kart</p>
