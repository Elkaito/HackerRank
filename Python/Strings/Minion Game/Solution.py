# Author: Kai Tanaka


def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    score_kevin = 0
    score_stuart = 0
    """
    Iterate through every char and check wheter it is a vowel or not.
    The total number of substrings possible starting from that char can be obtained by this formula:
    For a string str with len(str)=x and index i of str[i]
    len(x) - i

    Example:
    str = "BANANA" at i = 1 = A, len(str)=6
    => 6 - 1 = 5

    # of all possible substrings are = 5:
    ANANA
    ANAN
    ANA
    AN
    A
    """
    
    # Count the number of substrings for each player
    for i in range(0,len(string)):
        if string[i] in vowels:
            score_kevin += len(string) - i
        else:
            score_stuart += len(string) - i
            
    # Print winner
    if score_kevin == score_stuart:
        print("Draw")
    elif score_kevin > score_stuart:
        print("{} {}".format("Kevin",score_kevin))
    else:
        print("{} {}".format("Stuart",score_stuart))
    