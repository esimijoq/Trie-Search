from os import link
import requests


texts = ["What a truly wonderful day! The sun is shining, birds are singing, and everything feels absolutely perfect. I'm filled with immense joy and gratitude. Life is beautiful.", "This new restaurant is simply fantastic! The food was delicious, the service impeccable, and the atmosphere delightful. I highly recommend it; a truly enjoyable experience overall.", "Today has been utterly miserable. The rain poured incessantly, my internet kept crashing, and I felt completely overwhelmed. A truly frustrating and disappointing day.", "I'm so incredibly upset with this product. It broke almost immediately, the support was unhelpful, and I feel completely ripped off. A terrible purchase, I regret it."]

texts_new = []
for text in texts:
  text_new = text.replace(".", "").replace("!","").replace(",","").replace("'","")
  texts_new.append(text_new)


with open("/content/drive/MyDrive/Colab Notebooks/texts.txt", 'r') as file:
  f = file.read()
  text_txt = f.split("\n\n")

texts_from_txt = []
for text in text_txt:
  text_new = text.replace(".", "").replace("!","").replace(",","").replace("'","").replace(";", "").replace("\n", "")
  texts_from_txt.append(text_new)

for text in texts_from_txt:
  texts_new.append(text)

texts_new_split = []
for text in texts_new:
  txt = text.split(" ")
  texts_new_split.append(txt)

print(texts_new_split)

trie = {}
for text in texts_new_split:
  for word in text:
    dictionary = trie
    for char in word:
      if char not in dictionary:
        dictionary[char] = {}
      dictionary = dictionary[char]
    dictionary["end"] = True
print(trie)

def search(word):
    current = trie
    for char in word:
      if char not in current:
        return False
      current = current[char]
    return current["end"]

print(search("sun"))

def prefix(trie, prefix_word):
    current = trie
    for char in prefix_word:
        if char not in current:
          return []
        current = current[char]

    results = []
    def autocomplete(word, prefix_char):
      for char, next in word.items():
        if char == 'end':
          results.append(prefix_char)
        else:
          autocomplete(next, prefix_char + char)
          
    autocomplete(current, prefix_word)
    return results

print(prefix(trie, "s"))
print(prefix(trie, "su"))
print(prefix(trie, "wo"))
