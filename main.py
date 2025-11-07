# refactoring means to resturcture code without chanigng its external behavior This helps improve code readability and maintainability
from problem_set1 import problem1
from advance_slicing import advanced_slice
from extract_info import ex_info
from string_methods import str_methods
from problem_set4 import problem4
problem1()
advanced_slice()
ex_info()
str_methods()
problem4()




magic = "abracadabra"
print(magic[4])
print(magic[-2])
print(magic.index('c'))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
hij = alphabet[7:10]
print(alphabet[7:10])
print(alphabet[:13:2])
print(alphabet[::-1])
speech =  "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(speech.find('John F. Kennedy'))
speech_name = speech[83:]
print(speech_name)

info = "Python is fun. Fun is good. Good is subjective."
print(info.rfind('subjective'))
subjective_wrd = info[36:]
print(subjective_wrd)
every_third = info.split()[::3]
reversed_words = ' '.join(info.split()[::-1])
print(reversed_words)
text = "MAY THE FORCE BE WITH YOU."
lower_text = text.lower()
print(lower_text)
motto = ["Make", "haste", "slowly."]
joined_motto = ' '.join(motto)
split_on_a = joined_motto.split('a')
print(split_on_a)

sentence = "Life is what happens when you are busy making other plans."
replaced_busy = sentence.replace("busy", "distracted")
replaced_plans = sentence.replace("plans", "mistakes")
print(replaced_plans)
print(replaced_busy)

word = "Iteration"
repeated_word = word * 7

quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
has_moonlight = "moonlight" in quote2
print(has_moonlight)

phrase = "Supercalifragilisticexpialidocious"
num_chars = len(phrase)
count_i = phrase.count('i')
print(count_i)