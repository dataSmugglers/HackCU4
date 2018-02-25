import re
import statistics

unsorted = {"fucker": 8, "you": 3, "scumbag": 24}
keys = ["fucker","you","scumbag"]
vals=[8,3,24]

sort_vals=[24,24,8,3]


# Use to remove 'hastags' from user input strings.
# This way we can properly recognize the words
# Uses the python regular expression library
def remove_pound(user_input):
    new_user_input = re.sub('[#]', '', user_input)
    return new_user_input


# create list of words (word is key, number of instances is value)
# if words exists increment its value
# else continue
# returns a dictionary
def count_words(twitter_post):
    return_dict = {}
    word_list = twitter_post.split(" ")
    for word in word_list:
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
    return_list = [sorted_keys, sort_vals]
    return return_list


# our total sample size
# (number of posts we are working with)
def get_sample(twitter_post_list):
    return len(twitter_post_list)


# The difference between the largest and smallest value
def get_range(occurence_list):
    return occurence_list[0] - occurence_list[len(occurence_list)-1]


# the most common recurring value (number)
def get_mode(occurrence_list):
    return statistics.mode(occurrence_list)


# the middle value
def get_median(occurence_list):
    return statistics.median(occurence_list)

# the average value
def get_mean(occurence_list):
    return statistics.mean(occurence_list)

print(str(order_list(unsorted)))
print(get_range(sort_vals))
print(get_mode(sort_vals))
print(get_median(sort_vals))
print(get_mean(sort_vals))
