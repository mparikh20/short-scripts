
# Find a news article, put the text in a file. Then, get the word frequency for each word, and output that into another file as a csv. Try to use the csv module.

# Read the file.
# Iterate over each line.

# WORD CLEANER FUNCTION
# A function that takes a list of words and iterates through the list to produce a list of cleaned up words without special characters.
# Tested this on testlist = ["age-related,","Diseases","FGF34",'exists."'] --> ['age', 'related', 'diseases', 'fgf34', 'exists']
def wordcleaner(wordlist):
    cleaned_list = []
    for word in wordlist:
        word = word.lower()
        word = word.strip('"').strip(".").strip(",").strip("(").strip(")")
        if word.count("-") > 0:
            dehyphened = word.split("-") # eg. ["age","related"]
            cleaned_list = cleaned_list + dehyphened
        else:
            cleaned_list.append(word)
    return(cleaned_list)


# FINAL CODE
news = open('article.txt')
dict_words = {}
all_words = []
for line in news:
    line = line.strip('\n') #removes newline character # line could be an entire paragraph.
    words_ls = line.split(" ") #splits words/phrases by spaces. List of elements. ["Several","Age-Related,","Diseases,"]
    all_words = all_words + wordcleaner(words_ls) #Runs the list to clean up all the words. This now is a list consisting of cleaned up words from 1 para.
for word in all_words:
    if word not in dict_words.keys():
        dict_words[word] = all_words.count(word)
results = open("extractedwords.csv","w")
for item in dict_words.items():
    word,count = item
    results_content = word + "," + str(count) + "\n"
    results.write(results_content)
news.close()
results.close()


