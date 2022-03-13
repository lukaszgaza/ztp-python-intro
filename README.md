# Python Intro

1. Poprawne rozwiązanie powinno przechodzić wszystkie testy uruchomione za pomocną `python -m unittest`

2. Zaimplementuj klasę `Person`
* kod klasy ma znajdować się w pliku `person.py`
* klasa ma reprezentować osobę
* klasa ma przyjmować jako argumenty konstruktora `name` i `surname`
* klasa ma posiadać metodę `say_hello()` zwracającą ciąg znaków `Hello! I am <name> <surname>` gdzie `name` i `surname` to parametry przekazane do konstruktora

3. Zaimplementuj następujące metody
* metody powinny znajdować się w pliku `utils.py`
* metoda `second_max()` powinna przyjmować jako swój argument listę liczb i powinna zwrócić drugą największą wartość w tej liście, jeżeli lista ma niewystarczającą długość metoda powinna zwrócić `None`
* metoda `odd_even_count` powinna przyjmować jako swój argument listę i powinna zwracać tuple (krotkę) której wartościami są odpowiednio liczba wartości nieparzystych i parzystych w przekazanej liście