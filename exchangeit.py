"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Derek Palmer
Date:   01/03/2022
"""

import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = float(input('Amount of the original currency: '))

exchanged = currency.exchange(src,dst,amt)
exchanged = round(float(exchanged),3)

print('You can exchange ' + str(amt)+ ' ' + src +' for ' + str(exchanged)+ ' ' + dst + '.')