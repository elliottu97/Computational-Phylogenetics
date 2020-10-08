A = str(input("Input Sequence A"))
B = str(input("Input Sequence B"))
C = str(input("Input Sequence C"))

if len(A) != len(B) or len(A) != len(C) or len(B) != len(C):
    print("Error, sequences must be the same length")
    exit()

letters = ["A" , "C" , "G" , "T"]
for char in A:
    if (char not in letters):
        print("Error, sequences can only contain A, C, G, or T")
        exit()

for char in B:
    if (char not in letters):
        print("Error, sequences can only contain A, C, G, or T")
        exit()

for char in C:
    if (char not in letters):
        print("Error, sequences can only contain A, C, G, or T")
        exit()

def hamming(s1, s2):
    """Calculate the Hamming distance between two strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

if hamming(A, B) < hamming(B, C) and hamming(A, B) < hamming(A, C):
    print("Speices A and B have the most recent common ancestor.")

elif hamming(A, C) < hamming(B, C) and hamming(A,C) < hamming(A,B):
    print("Species A and C have the most recent common ancestor")

elif hamming(B, C) < hamming (A, B) and hamming(B, C) < hamming(A, C):
    print("Species B and C have the most recent common ancestor")

else:
    print("There are the same number of differences in all 3 sequences.")