from string import ascii_lowercase

def solution(s):
    al = list(ascii_lowercase)
    return False if sorted(s.lower())[-1] in al or len(s)!=4 and len(s)!=6 else True