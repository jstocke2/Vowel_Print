###################################################################
#Jake Stocker                                                     #
#07/11/2014                                                       #
#                                                                 #
#This program counts how many words from file words.txt           #
#contain the vowels a e i o u in sequential order                 #
#                                                                 #
#                                                                 #
#Further functionality:  If needed edit variable vowels to find   #
#other pieces of text in sequential order                         #
###################################################################


###IMPORTANT###You will need to modify the directory of the file for your hardrive


fin=open("/home/jake/Desktop/words.txt")
LINE=fin.readline
VOWELS="aeiou"

#This function returns true if every letter of string lettersCompared can be matched with every
#letter in the string word in order


def contains_letters_in_order(word, lettersCompared):
    matches = 0
    for letter in word:
        if letter == lettersCompared[matches]:
            matches += 1
            if matches == len(lettersCompared):
                return True
    return False


#Main() reads all lines in the file and then tests each string passed by contains_vowels_in_order()
#if the string contains all letters of string lettersCompared in order the word is printed.  


def main():
    count=0
    for LINE in fin:
        if contains_letters_in_order(LINE,VOWELS)==True:
            print LINE
            
                   



main()

          
      
    
    
    



