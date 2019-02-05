#!/usr/bin/env python3

#--------------------------------------------
# Title: kata 14, trigrams (from lesson 4)
# Changelog:
# 2019-02-04,Aaron Devey,Created
#--------------------------------------------

import re
import random

trigrams = {}

def ingest_file(filename):
  f = open(filename, "r")
  contents = f.read()
  sentences = re.split(r'[.?!;]+', contents)
  for sentence in sentences:
    process_sentence(sentence)

def process_sentence(sentence):
  words = re.split(r'\s+', sentence)
  counter = 0
  while len(words[counter:counter+3]) == 3:
    process_trigram(words[counter:counter+3])
    counter += 1

def process_trigram(trigram):
  tup = tuple(trigram[0:2])
  word = trigram[2:3]
  if tup in trigrams:
    trigrams[tup] += word
  else:
    trigrams[tup] = word

def pick_next_word(pair):
  if pair in trigrams:
    choices = trigrams[pair]
    return(random.choice(choices))
  return(None)

def generate_sentence():
  start_words = list(random.choice(list(trigrams.keys())))
  sentence = start_words[0] + " " + start_words[1]
  next_word = pick_next_word(tuple(start_words))
  previous_words = start_words
  while next_word != None:
    sentence = sentence + " " + next_word
    previous_words = [previous_words[1], next_word]
    next_word = pick_next_word(tuple(previous_words))
  return(sentence.capitalize())

def main():
  i = None
  while i != "3":
    print("-" * 70)
    print("Choose:")
    print("1. Ingest a text file")
    print("2. Generate a sentence")
    print("3. Quit")
    i = input("Enter a choice, 1,2,3: ")
    if i == "1":
      file = input("Enter a filename: ")
      print("Ingesting file: " + file)
      ingest_file(file)
      print("Ingest complete.")
    elif i == "2":
      print("Here is your sentence: " + generate_sentence())
    elif i == "3":
      print("Ok, goodbye!")
    else:
      print("Sorry, '" + i + "' is not a valid selection.")

if __name__ == "__main__":
  main()
