def chaine(poly):

    degre = poly[0]

    bits = ""
    for i in range(degre, -1, -1):

        if i in poly:
            bits += "1"
            del poly[0]
        
        else:
            bits += "0"

    return bits


def xor(mot1, mot2):

    taille1 = len(mot1)
    taille2 = len(mot2)

    if taille1 > taille2:
        mot2 += "0" * (taille1 - taille2)
        taille = taille1

    else:
        mot1 += "0" * (taille2 - taille1)
        taille = taille2

    mot = ""
    for i in range(taille):
        mot += str((int(mot1[i]) + int(mot2[i])) % 2)

    return mot


def div_eucl(msg, div):

    taille_d = len(div)

    msg += "0" * (taille_d - 1)
    taille_m = len(msg)

    reste = msg
    for i in range(taille_m):

        if reste[i] == "1":
            reste = xor(reste[i :], div)

    return "0" + reste[taille_m - taille_d :]


def initial(msg, gen):

    return msg[: len(msg) - len(gen) + 1]


# Exercice 1 :

gx = [6, 4, 1, 0]
nx = "101011000110"

# 1)
generateur = chaine(gx)
print("G(x) = " + generateur)

# 2)
reste = div_eucl(nx, gx)

if int(reste) == 0:
    lx = initial(nx, generateur)
    print("Le message reçu est correct,\nlx = " + lx)

else:
    print("Le message reçu n'est pas correct.")


# Exercice 2 :

gx = [16, 12, 5, 0]
generateur = chaine(gx)
message = "0100000000000000010101100010011110011110"

reste = div_eucl(message, generateur)

if int(reste) == 0:
    print("Le message a été reçu sans erreur")

else:
    print("Il y a une erreur")
