

import re

def is_orderered(input, ordering):
    pattern = "[^{0}]".format(ordering)
    matches = re.sub(pattern, '', input)
    uniques = []
    [uniques.append(s) for s in matches if s not in uniques]
    uniques = ''.join(uniques)
    if uniques == ordering:
        return True
    else:
        return False


print is_orderered('cocmmputreraa', 'cmpr')
