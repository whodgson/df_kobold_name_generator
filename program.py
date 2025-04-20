import word_gen

language_words = []

with open("words.txt","r") as file:
    language_words = [line.strip() for line in file]

output_file = open("language_kobold.txt","w")

output_file.write("language_kobold\n")
output_file.write("\n")
output_file.write("[OBJECT:LANGUAGE]\n")
output_file.write("\n")
output_file.write("[TRANSLATION:KOBOLD]\n")

for language_word in language_words:
    kobold_word = word_gen.get_kobold_word(language_word)
    output_file.write(f"\t[T_WORD:{language_word}:{kobold_word}]\n")

output_file.close()

review_file = open("language_kobold.txt","r")
print(review_file.read())