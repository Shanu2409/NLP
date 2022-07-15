from collections import Counter
import string
import matplotlib.pyplot as plt


# cleaning text by removing punctuation
text = open('say.txt', encoding='utf-8').read()
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenization and Stop Words
t_text = text.split()


# stop Words

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

f_word = []

for word in t_text:
    if word not in stop_words:
        f_word.append(word)


#replace words with its emotions

emo_list = []

with open('emotions.txt', 'r') as file:
    for line in file:
        clear = line.replace('\n', '').replace(',', '').replace('\'', '').strip()
        word, emotions = clear.split(':')
        if word in f_word:
            emo_list.append(emotions)


#counting all emotions
x = Counter(emo_list)
#print(x)

fig , ax = plt.subplots()
ax.bar(x.keys(), x.values(), color='#7eb54e')
fig.autofmt_xdate() #auto alignment of x axis
plt.savefig('graph.png')
plt.title('Emotions found in life story of Nikola Tesla', fontstyle='italic',
          backgroundcolor='#F0F0EE', pad=10)
plt.show()