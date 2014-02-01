import pdb
import random
import string

# exemple:
# Tirage : S I N U S A M O R
# 2 Solutions possibles en 9 lettres :
# MARSOUINS
# SOUS-MARIN

# From man
     #   0 nul    1 soh    2 stx    3 etx    4 eot    5 enq    6 ack    7 bel
     #   8 bs     9 ht    10 nl    11 vt    12 np    13 cr    14 so    15 si
     #  16 dle   17 dc1   18 dc2   19 dc3   20 dc4   21 nak   22 syn   23 etb
     #  24 can   25 em    26 sub   27 esc   28 fs    29 gs    30 rs    31 us
     #  32 sp    33  !    34  "    35  #    36  $    37  %    38  &    39  '
     #  40  (    41  )    42  *    43  +    44  ,    45  -    46  .    47  /
     #  48  0    49  1    50  2    51  3    52  4    53  5    54  6    55  7
     #  56  8    57  9    58  :    59  ;    60  <    61  =    62  >    63  ?
     #  64  @    65  A    66  B    67  C    68  D    69  E    70  F    71  G
     #  72  H    73  I    74  J    75  K    76  L    77  M    78  N    79  O
     #  80  P    81  Q    82  R    83  S    84  T    85  U    86  V    87  W
     #  88  X    89  Y    90  Z    91  [    92  \    93  ]    94  ^    95  _
     #  96  `    97  a    98  b    99  c   100  d   101  e   102  f   103  g
     # 104  h   105  i   106  j   107  k   108  l   109  m   110  n   111  o
     # 112  p   113  q   114  r   115  s   116  t   117  u   118  v   119  w
     # 120  x   121  y   122  z   123  {   124  |   125  }   126  ~   127 del

wordListFromDict = []
charsTirage = []
solutionWords = ["dickbutt"]


# La shit goes in here
def main():
    openDickAndFillWordsWithCaps()

    # On cre 9 charsTirage random
    for x in range(0, 9):
        # randint a convertir en char pour donner une lettre (et ajouter 45
        # pour tiret, fuuu)
        randLetter = chr(random.randint(65, 90)) 
        """for i in range(0, len(charsTirage)): #eviter repetitions (non fonctionnel)
            while charsTirage[i] == randLetter:
                randLetter = chr(random.randint(65, 90))
                charsTirage[i] = randLetter"""
        charsTirage.append(randLetter)

    
    print "Tirage :",charsTirage # a imprimer sans larray, imanoob
    

    # ici, on doit looper et essayer de trouver le plus de mots avec le plus de lettres
    # possible
    for x in range(0, 9):
        for word in wordListFromDict:
            wordHasAllLetters = True #vrai par defaut
            
            for char in charsTirage:
                if char not in word:
                    wordHasAllLetters = None #faux si pas trouve
                    break
            if wordHasAllLetters:
                solutionWords.append(word)
        #charsTirage.pop(0) #Foncionne pas, spaaaaaaaaaaaaaaaaaaaaam

    print len(solutionWords), "Solutions possibles en 9 lettres :"
    for solution in solutionWords:
        print solution

    # pdb.set_trace()


# a la fin, la solution doit etre affiche en ordre alphabetique
def reordonnerAlphabetiquement(array):
    """
    >>> reordonnerAlphabetiquement(["ABC", "AAA", "CCC"])
    ["AAA", "ABC", "CCC"]
    """
    return array # needs to be sorted dude!



def openDickAndFillWordsWithCaps():
    f = open('Dictionnaire.txt')

    for word in f:
        # ca enleve la shit de fin de ligne au moins lol
        wordListFromDict.append(
            str(word).replace("\n", "").replace("\r", "").upper()
            )





# appel la fonction main dude, occupe toi pas de ca
if __name__ == "__main__":
    main()
