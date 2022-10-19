def decrypt_caesar_cipher(sentence, n):
    sentence = list(sentence.strip(" "))
    for i in range(len(sentence)):
        alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for j in range(len(alphabet_upper)):
            if sentence[i] == alphabet_upper[j]:
                sentence[i] = alphabet_upper[j - n]
                break
            elif sentence[i] == alphabet_lower[j]:
                sentence[i] = alphabet_lower[j - n]
                break
    sentence = "".join(sentence)
    return sentence
print(decrypt_caesar_cipher("Aopz pz h zljyla", 7))

#Ex10
def game_with_cells(m, n):
    if m>=2 and n>=2:
        if m*n%4 == 0:
            num = m*n//4
        elif m*n%2 == 0 and m*n%4 != 0:
            num = m*n//4 + m%n//2
        else :
            num = (m//2*2)*(n//2*2)/4 + m//2+n//2 + m*n%2
    elif m>1 or n>1:
        if (m%2 == 0 and n<2) or (n%2 == 0 and m<2):
            num = m*n//2
        elif m%2 != 0 and n%2 != 0:
            num = m*n//2 + m%n
    else:
        num = 1
    return num
print(game_with_cells(10, 1))
