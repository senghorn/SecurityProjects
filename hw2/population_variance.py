def p_variance(frequency, all_chars):
    total = 0.0
    for x in frequency:
        total+= frequency[x]

    N = len(all_chars)
    mean = total/N
    sum = 0.0
    for char in all_chars:
        hz = frequency[char]
        curr = hz - mean
        curr *= curr
        sum += curr

    var_x =  sum/N
    return var_x

frequency = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }
all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
## print(p_variance(frequency,all_chars)) ## Q2.1