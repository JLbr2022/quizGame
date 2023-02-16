import random

tryDidIt = 0

print('¡Hola! ¿Cómo te llamas?')
myName = input()

number = random.randint(1, 20)
print('Bueno, ' + myName + ', estoy pensando en un número entre 1 y 20.')

while tryDidIt < 6:
    print('Intenta adivinar.')  # there are four spaces after print
    guessing = input()
    guessing = int(guessing)

    tryDidIt = tryDidIt + 1

    if guessing < number:
        print('Tu estimación es muy baja.')  # we have eight spaces after print

    if guessing > number:
        print('Tu estimación es muy alta.')

    if guessing == number:
        break

if guessing == number:
    tryDidIt = str(tryDidIt)
    print('¡Buen trabajo, ' + myName +
          '! ¡Has adivinado mi número en ' + tryDidIt + ' intentos!')

if guessing != number:
    number = str(number)
    print('Pues no. El número que estaba pensando era ' + number)
