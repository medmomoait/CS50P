from pyfiglet import Figlet
import sys
from random import choice 

x = Figlet()
y = x.getFonts()

if len(sys.argv) == 1:
    rf = choice(y)
    x.setFont(font = rf)

elif len(sys.argv) == 3:
    sf = sys.argv[2]
    if sys.argv[1] == '-f' or sys.argv[1] == '--font' and sf in y:
        x.setFont(font = sf)
    else:
        sys.exit('Invalid usage')

else:
    sys.exit('Invalid usage')

inpt = input('Input: ')
print('Output:', x.renderText(inpt), sep = "\n")