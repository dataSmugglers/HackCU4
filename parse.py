import re
import statistics

word_filter_list = ["","rt"]

# Use to remove 'hastags' from user input strings.
# This way we can properly recognize the words
# Uses the python regular expression library
def remove_pound(user_input):
    new_user_input = re.sub('[#]', '', user_input)
    return new_user_input


# Use this function to clean up the punctuation.
def remove_punc(single_word):
    new_user_input = re.sub('[#.!?,:;]', '', single_word)
    return new_new_user_input


# Check if a word if filtered
# Takes the list of all words, and their frequency list
# Returns a list of lists
def word_filter(word_list, freq_list):
    ret_list = []
    for target in word_list:
        if target in word_filter_list:
            indx = word_list.index(target)
            word_list.remove(target)
            freq_list.remove(indx)
    ret_list.append(word_list)
    ret_list.append(freq_list)
    return ret_list


# Takes a list of strings with puncuation and returns a list  of strings 
# without puncuation and lowercases
def clean_up(word_list):
  temp = []
  for word in word_list:
    if "//" not in word:
      derp = remove_punc(word)
      temp.append(derp.lower())
    else:
      temp.append(word)
  return temp


# create list of words (word is key, number of instances is value)
# if words exists increment its value
# else continue
# returns a dictionary
def count_each_word(twitter_post):
    return_dict = {}
    word_list = twitter_post.split(" ")
    cleaned_word_list = clean_up(word_list)
    for word in cleaned_word_list:
        if word not in return_dict:
            return_dict[word] = 1
        else:
            return_dict[word] = return_dict[word] + 1
    return return_dict

  
# Takes a dictionary of word -> count pairs
# returns a list of lists
# each list is sorted in descending order
def order_list(word_dict):
    sorted_vals = sorted(word_dict.values(), reverse=True)
    sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)

    return_list = [sorted_keys, sorted_vals]

    updated_list = remove_empty(return_list)
    return updated_list 

def remove_empty(key_val_list):
  key_val_list[0].pop(0)
  key_val_list[1].pop(0)
  return key_val_list
  
  

# Our Sample size
def get_sample(twitter_post_list):
    return len(twitter_post_list)


# The difference between the largest and smallest value
def get_range(occurence_list):
    return occurence_list[0] - occurence_list[len(occurence_list)-1]


# The most common recurring value (number)
def get_mode(occurrence_list):
    return statistics.mode(occurrence_list)


# The middle value
def get_median(occurence_list):
    return statistics.median(occurence_list)

# the 'average' value
def get_mean(occurence_list):
    return statistics.mean(occurence_list)
  