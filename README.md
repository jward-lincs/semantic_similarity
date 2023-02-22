# Semantic Similarity (NLP)
## This git contains compulsory task 1 and 2

- [Semantic Similarity (NLP)](#semantic-similarity--nlp-)
  * [This git contains compulsry task 1 and 2](#this-git-contains-compulsry-task-1-and-2)
- [Compulsory Task 1](#compulsory-task-1)
  * [Notes of interest regarding cat, money and banana similarities:](#notes-of-interest-regarding-cat--money-and-banana-similarities-)
  * [Notes on the difference between 'en_core_web_md'. ‘en_core_web_sm’:](#notes-on-the-difference-between--en-core-web-md---en-core-web-sm--)
- [Compulsory Task 2](#compulsory-task-2)
  * [watch_next.py](#watch-nextpy)
  * [Installation](#installation)
  * [Usage](#usage)


# Compulsory Task 1


Notes of interest regarding cat, money and banana similarities:
---------------------------------------------------------------

Although I wasn't surprised that the similarity between monkey and banana is nearly 
twice that of the cat and the banana (a book title I've yet to read...)
I was a little surprised that the similarity between and the cat and the monkey was
only 50% greater than the comparison of the money and banana. I expected it to be greater.

I tried a similar exercise with Mum, Dad and child. 
Although there was a strong similarity between mum and dad (0.786), 
I was surprise at the relatively low numbers for mum and child (0.125) and even worse: dad and child (0.066).



Notes on the difference between 'en_core_web_md'. ‘en_core_web_sm’:
-------------------------------------------------------------------
Because  ‘en_core_web_sm’ was looking specifically at words and not how they are used,
some of the the similarities within one list were higher than ‘en_core_web_sm’, some lower and some broadly the same. 

However, when comparing insurance claims and recipes, because 'en_core_web_md' wasn't looking
at the nuances and narrative of the text, if found much lower similarities possibly due to a lack of shared words groups.

# Compulsory Task 2
## watch_next.py
This program uses NLP to make a movie recommendation.

## Installation
Make sure that watch_next.py and movies.txt are in the same folder as each other.

## Usage
Run the program! It will use the text from the synopsis of 'Planet Hulk' in the program and work out the similarites to it in the movies.txt file. It then finds the most similar and prints out a recommendation to watch it.

