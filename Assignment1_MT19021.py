import re
import os
from nltk.tokenize import sent_tokenize, word_tokenize
#function to count no. of sentences and no. of words
def part_1(full_path):
    fp = open(full_path,"r")
    text = fp.read()
    fp.close()
    sentences = sent_tokenize(text)
    no_of_sentences = len(sentences)
    words = word_tokenize(text)
    no_of_words = len(words)
    return no_of_sentences,no_of_words

#function to count no. of words starting with a vowel and no. of words starting with a consonant
def part_2(full_path):
    fp = open(full_path,"r")
    text = fp.read()
    fp.close()
    words = word_tokenize(text)
    consonant_words = []
    for word in words:
        if word[0] not in "AaEeIiOoUu":
            consonant_words.append(word)
    no_of_consonant_words = len(consonant_words)
    
    vowel_words = []
    for word in words:
        if word[0] in "AaEeIiOoUu":
            vowel_words.append(word)
    no_of_vowel_words = len(vowel_words)
    
    return no_of_consonant_words, no_of_vowel_words

#function to list all emailids in the given file 
def part_3(full_path):
    fp = open(full_path,"r")
    text = fp.read()
    fp.close()
    email_ids = re.findall('\S+@\S+',text)
    print("The email ids in the file are:")
    print(email_ids)
    
#function to find no. of sentences starting with a aprticular word
def part_4(full_path,starts_with):
    fp = open(full_path,"r")
    text = fp.read()
    fp.close()
    sentences = sent_tokenize(text)
    sentence_start = 0
    for sentence in sentences:
        words = word_tokenize(sentence)
        if words[0] == starts_with:
            sentence_start = sentence_start + 1
    return sentence_start
    
def part_5(full_path,ends_with):
    fp = open(full_path,"r")
    text = fp.read()
    fp.close()
    sentences = sent_tokenize(text)
    sentence_end = 0
    for sentence in sentences:
        words = word_tokenize(sentence)
        if words[-2] == ends_with:
            sentence_end = sentence_end + 1
    return sentence_end

def part_6(full_path, word_occurence):
    fp = open(full_path,"r")
    text = fp.read()
    fp.close()
    words = word_tokenize(text)
    count_occurence = 0
    for word in words:
        if word == word_occurence:
            count_occurence = count_occurence + 1
    return count_occurence
    

print("Enter the filename:")
file_name = input()
full_path = os.path.join(r"D:\M.tech sem1\NLP\Assignments\A1\20news-19997", file_name)

no_of_sentences, no_of_words = part_1(full_path)
no_of_consonant_words, no_of_vowel_words= part_2(full_path)
print(f"The no. of sentences in the file is {no_of_sentences}")
print(f"The no. of words in the file is {no_of_words}")
print(f"The no. of words starting with a consonant are {no_of_consonant_words}")
print(f"The no. of words starting with vowels are {no_of_vowel_words}")
part_3(full_path)

print("Enter the filename to be checked for sentences starting with a particular word:")
file_name = input()
full_path = os.path.join(r"D:\M.tech sem1\NLP\Assignments\A1\20news-19997", file_name)
print("Enter the word to be checked in sentence starting")
starts_with = input()
sentence_start = part_4(full_path,starts_with)
print(f"No. of sentences staring with {starts_with} are {sentence_start}")

print("Enter the filename to be checked for sentences ending with a particular word:")
file_name = input()
full_path = os.path.join(r"D:\M.tech sem1\NLP\Assignments\A1\20news-19997", file_name)
print("Enter the word to be checked in sentence ending")
ends_with = input()
sentence_end = part_5(full_path, ends_with)
print(f"No. of sentences ending with {ends_with} are {sentence_end}")
        
print("Enter the filename to be checked for occurence of a particular word:")
file_name = input()
full_path = os.path.join(r"D:\M.tech sem1\NLP\Assignments\A1\20news-19997", file_name)
print("Enter the word to be checked for no. of occurences")
word_occurence = input()
count_occurence = part_6(full_path, word_occurence)
print(f"{word_occurence} appears {count_occurence} times in the file")




