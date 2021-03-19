import ex25_module
sentence = "All good things come to those who wait"
words = ex25_module.break_words(sentence)
print(words)
sorted_words = ex25_module.sort_words(words)
print(sorted_words)
ex25_module.print_first_word(words)
ex25_module.print_last_word(words)
sorted_words = ex25_module.sort_sentence(sentence)
print(sorted_words)
ex25_module.print_first_and_last(sentence)
ex25_module.print_first_and_last_sorted(sentence)
