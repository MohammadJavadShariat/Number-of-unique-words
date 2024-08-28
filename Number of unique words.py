Str = input("Suggested text (Hello friends, I hope you are doing well. Friends, the seventh session of the Python class will be held today at 18:00. I hope it will be useful for you.)\nEnter your text:\n ")

#Remove points from text
Str2 = Str.replace(".","")
#Verbatim text
string = Str2.split()

#Putting all the words of the text in 
#the set and removing the duplicate words
Word = set()
for i in string :
    Word.add(i)

#Print the non-repeated words of the text and their number
#Sentence if there are more than one words
if len(Word) > 1 :
    print(f"\n{Word}")
    print((f"\n*******Number of words*******\nThe number of non-repeating words in the {len(Word)} text is up to."))

#If the text is one word
elif len(Word) == 1 :
    print(f"\n{Word}")
    print(("\n*******Number of words*******\nThe number of non-repetitive words in the text is one."))

#If no words are entered
elif len(Word) == 0 :
    Word = "not available!"
    print(f"\n{Word}")
    print("\n********Number of words********\nThere are no non-repeating words!")