## counting DNA nucleotides

# count A, C, G, T in a given string

from itertools import count

DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

a_count = DNA.count("A")
c_count = DNA.count("C")
g_count = DNA.count("G")
t_count = DNA.count("T")

print(a_count)
print(c_count)
print(g_count)
print(t_count)
