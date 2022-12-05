### CHAINING OF COMPARISSON OPERATORS
# Neu


def ensure_within(value, bounds):
    m, M = bounds
    print(type(bounds))
    return m <= value <= M


print(ensure_within(3, [4, 5]))  # bound == list
print(ensure_within(3, {4, 5}))  # bound == set
print(ensure_within(3, (4, 5)))  # bound == tuple


"""
a = 3
b = [3, 5]
if (a in b) == True:
    print("Yeah")
else:
    print("Noooo")


a = True
b = True
c = True

if a == b == c:
    print("Auf einer Welle")
else:
    print("Achtung wir müssen eine Lösung finden.")

### BENENNUNG VON VARIABLEN, FUNKTIONEN UND KONSTANTEN

def myfunc(a):
    empty = []
    for i in range(len(a)):
        if i % 2 == 0:
            empty.append(a[i].upper())
        else:
            empty.append(a[i].lower())

    return "".join(empty)


print(myfunc("Anthropomorphism"))


def alternate_casing(text):
    letters = []
    for idx in range(len(text)):
        if idx % 2 == 0:
            letters.append(text[idx].upper())
        else:
            letters.append(text[idx].lower())
    return "".join(letters)


print(alternate_casing("What is going on?"))
"""
