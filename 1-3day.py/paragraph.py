paragraph = input("Enter a paragraph: ")

words = paragraph.split()

# Count words
word_count = len(words)

# Find largest word
largest_word = ""
for word in words:
    if len(word) > len(largest_word):
        largest_word = word

# Count vowels
vowels = 0
for ch in paragraph.lower():
    if ch in "aeiou":
        vowels += 1

print("Total Words:", word_count)
print("Largest Word:", largest_word)
print("Number of Vowels:", vowels)