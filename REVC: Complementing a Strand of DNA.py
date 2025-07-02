## complementing a strand of DNA
# change A to T, change C to G and make a reverse order
DNA_3 = "AAAACCCGGT"
DNA_4 = ""
for i in DNA_3:
    if i == "A":
        DNA_4 = DNA_4 + "T"
    elif i == "C":
        DNA_4 = DNA_4 + "G"
    elif i == "G":
        DNA_4 = DNA_4 + "C"
    else:
        DNA_4 = DNA_4 + "A"
print(DNA_4)
# make reverse
print(DNA_4[::-1])
