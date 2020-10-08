# Computational-Phylogenetics
Basic genetic distance calculator, can determine between three equal length "strings of DNA" (using A, C, G, &amp; T) which two have the most recent common ancestor. Uses for loop, len function, and hamming distance.
Assignment Instructions
  First, the user needs to enter three different strings which correspond to three different DNA sequences A, B and C. 
    You should ensure that the entered strings are actually valid DNA sequences.
    In particular, after the user enters the DNA sequences, you should validate that
      1. all sequences include no characters other than "A", "C", "G" and "T", and
      2. all sequences have the same length.
    If the sequences entered by the user are not validated, you should print an error message and quit the program immediately with the statement "exit()".
    
   Second, After the input sequences have been entered and validated, you should compute the genetic distance. 
    There are different ways to determine the genetic distance between two DNA sequences.
    We will assume that the sequences always have the same length and use the Hamming Distance 
    which compares two strings character-by-character and counts all the letters that are different. 
    For example, the distance between "AAC" and "ACC" is 1 because the two strings differ in their second character. 
    The distance between "AGG" and "GAA" is 3 because all three characters are different. 
    Given the three strings from the user input, first determine the distance between A and B. 
    You might want to use a for loop based on the length of A. As mentioned above, you can assume all strings have the same length. 
    Then, you can copy and paste the same code and modify it to calculate the distance between A and C and between B and C.
      Example: If A is "ACC", B is "CAT" and C is "GAT", then the distance between A and B is 3 (all characters are different), 
      the distance between A and C is also 3 and the distance between B and C is 1 (because only the first character is different).
      
    Third, The next step is to use the genetic distance matrix (Links to an external site.)
      In our case, we only have three different DNA sequences, so there can only be four different trees. 
      We can determine the correct tree by finding the two out of these three species that are the most similar, 
      so the two DNA sequences whose genetic distance is the smallest, the third sequence must therefore have an earlier common ancestor. 
      As a special case, it is also possible that two or more distances are tied. In each of these cases, print an according message.
      
     Example Interaction
     > DNA Sequence A:
      < GGACCT
     > DNA Sequence B:
      < CAACCT
     > DNA Sequence C:
      < GAAATT
     > Species A and B have the most recent common ancestor.
