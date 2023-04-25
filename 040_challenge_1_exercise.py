# Video alternative: https://github.com/makersacademy/intro-to-python/blob/main/999_video_index.md

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.
#check word length
  #report all word more than 10 letters but dont contain hyphen
  #if words longer than 15 letter shorten to 15 letters adn add ...
  
# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

# function that checks the length and hyph of a string 
def is_long_word (word):
  return len(word) > 10 and '-' not in word 
#function that checks the length of a string and manupulate it
def shorten_super_long_word(word):
  if len(word)> 15:
    return word[:15]+'...'
  else:
    return word
#function that reports the word
def report_long_words(words):
  #filtered words from the input using the filter keyword
  filtered_words= filter(is_long_word, words)
  #mapping over the filtered words and manipulating them as per ther requirement
  mapped_words = map(shorten_super_long_word, filtered_words)
  #using jouin to concatinate the mapped words in to comma seprated string to use as variable in return ststement
  long_words= ', '.join(mapped_words)
  return f'These words are quite long: {long_words}'


  
  # 
  
   

  #1 filter words longer than 10ch and non hyphenaed and assign to a new varia
  #2 loop the new variable for words longer than 15ch
    #2.1 if longer than 15 cap at 15 and add ...
  #output all long words to a string


  


check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
