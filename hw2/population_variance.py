def p_variance(fr, alphabets):
    total = 0.0
    for x in fr:
        total+= fr[x]
    N = len(alphabets)
    mean = findmean(fr.values())
    sum = 0.0
    for char in alphabets:
        hz = fr[char]
        curr = hz - mean
        curr = curr**2
        sum += curr
    return sum/N

def findmean (arr):
    return sum(arr)/len(arr)

frequency = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }
all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
## print("{:.4E}".format(p_variance(frequency,all_chars))) ## Q2.1