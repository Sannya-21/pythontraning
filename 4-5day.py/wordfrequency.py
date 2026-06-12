# Word Frequency Counter

paragraph = input("Enter a paragraph: ")

words = paragraph.lower().replace(".", "").replace(",", "").split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:")
print(freq)

top5 = sorted(freq.items(),
              key=lambda x: x[1],
              reverse=True)[:5]

print("Top 5 Most Frequent Words:")

for word, count in top5:
    print(word, ":", count)
    