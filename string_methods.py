def str_methods():
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
