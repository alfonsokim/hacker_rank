
MAX = 999999

TENS = [None, 'ten', 'eleven', 'twelve', 'thridteen', 'fourteen', 'fifthteen']
UNITS = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# =============================================================================
def to_english(num):
    if num > MAX:
        return 'Not today'
    words, remaining = [], num
    for i in range(5, 0, -1):
        relative = 10 ** i
        if remaining > relative:
            absolute = remaining % relative
            print relative, absolute


# =============================================================================
if __name__ == '__main__':
    to_english(152)
