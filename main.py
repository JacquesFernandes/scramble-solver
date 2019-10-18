#! /usr/bin/python3
from sys import argv;

try:
  from enchant import Dict;
except ModuleNotFoundError as mnfe:
  print("ERROR: The 'enchant' module (from PyEnchant) was not found!");
  exit(1);

dictionary = Dict("en_US");

isWord = lambda word: dictionary.check(word.lower());

def nBase(value: int, base: int, pad_to_output_length=0) -> [int]:
  bits = [];

  while value != 0:
    bits.insert(0, value%base);
    value = int(value/base);
  
  if pad_to_output_length > len(bits):
    padding = [0] * (pad_to_output_length - len(bits)); 
    bits = padding + bits;
  
  return bits;

def getCombinationsFor(letters: [str], target_word_length: int) -> [str]:
  combinations = set();
  max_num_combinations = len(letters) ** target_word_length;

  for i in range(max_num_combinations):
    data = nBase(i, len(letters), target_word_length);
    chars = [ letters[d] for d in data ];
    string = "".join(chars).lower();
    if isWord(string):
      combinations.add(string);
  
  return list(combinations);

if __name__ == "__main__":
  letters = argv[1:];
  letters = letters if len(letters) > 0 else input("Enter the characters separated by spaces: ").split(" ");
  letters = [ letter for letter in letters if letter.isalpha() ];
  
  target_word_len = input("Length of words to find: ");
  while target_word_len.isnumeric() == False:
    target_word_len = input("That isn't a number, try again: ");
  target_word_len = int(target_word_len);
  
  combinations = getCombinationsFor(letters, target_word_len);

  for combination in combinations:
    print(combination);
    