import nltk
import os
from nltk.tokenize import word_tokenize
import nltk.corpus
from nltk.probability import FreqDist
from nltk.corpus import cess_cat
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

lemmatizer = WordNetLemmatizer()


# print(os.listdir(nltk.data.find("corpora")))
# print(cess_cat.words())
# print(nltk.corpus.gutenberg.fileids())
# para = nltk.corpus.gutenberg.words('bible-kjv.txt')
# print(para)
#
# for i in para[10]:
#     print(i, sep=' ', end='')

tesla = """ If we ask you to look up the encyclopedia and find out who invented the radio or X-rays, neon lights that we use so often in the parties or the microwave that we use every day in the kitchen, you will never find anything about Nikola Tesla there. But the fact is otherwise! It was Nikola Tesla who did the main homework for the development of all the aforementioned things and the technology behind them. Yes, whether you believe it or not, the truth is that even though Tesla lived about a hundred and sixty years ago, he helped in developing technology that is used by all of us every single day. Sadly, he was never given the credit he truly deserved due to some unfortunate circumstances.

Early childhood
Nikola Tesla was born on July 10, 1856 in Smiljan, Croatia. His mother was an inventor and his father was a priest. His parents wanted him to become a priest like his father, but he had a passion for studying Science. He studied Science at the University of Prague and then started working for the Central Telephone Exchange in Budapest.

Tesla and Edison
At the age of 28, Tesla decided to go to America in pursuit of his desire to create new inventions. Upon moving to the United States, Tesla started working with the famous American inventor, Thomas Edison. While working together, a disagreement occurred between Tesla and Edison over Edison’s direct current and Tesla’s alternating current. This was also known as the “war of the currents.” Edison lamps were supplied with direct current which made them weak and inefficient. The direct current could not travel for long distances. On the other hand, Tesla’s alternating current was able to travel long distances on distribution lines, first in one direction, and then in another in multiple waves.

Tesla Electric Light Company
The disagreements created a lot of bitterness between the two scientists and Tesla eventually left Edison to create his own company called the Tesla Electric Light Company. His work caught the attention of another American inventor, George Westinghouse. They joined hands and started working together to generate electricity for the nation. Edison and Tesla were now in direct competition for providing America with energy and power. In 1893, Tesla’s AC electrical system was selected over Edison’s at the World’s Columbian Exposition in Chicago. It was a big accomplishment for Tesla. But, as luck would have it, Westinghouse ran into financial trouble and Tesla had to walk out of the partnership by selling his patent.

Wireless Broadcasting System
A year later, in 1896, Tesla created the world’s first hydroelectric power plant, which brought power to the city of Buffalo, New York. This invention brought Tesla considerable fame and recognition for a short while. During 1899 to 1900, Tesla continued to experiment with electricity and radio frequency magnetic waves in his laboratory based in Colorado. In 1900, supported by financier J.P. Morgan, Tesla started construction of a “Wireless Broadcasting System” tower on Long Island, New York. The aim of constructing this tower was to connect telephone and telegraph services, as well as broadcast images, reports, and weather information to every corner of the world. But due to certain reasons, J.P. Morgan had to cut funding and the tower had to be sold off.

Research gets stolen!
Tesla never had the gods of destiny working in his favor and there was more to come. During this period of turmoil, Tesla’s research work was stolen and used as their own by his contemporary scientists. Marconi is alleged to have passed off Tesla’s work on long-distance radio transmission as his own. Tesla decided to sue Marconi but it was too late. Though Tesla’s patents were prior to Marconi, the national press was out rightly supporting Marconi and the judge did not know a thing about modern technology. Naturally, Tesla lost his case. Much Later, in 1943, the US Supreme court conducted a detailed investigation, reversed the old decision given by the court and granted recognition to Tesla, nullifying Marconi patents.

Death
You would be surprised to know that Tesla had over 800 different patents to his name, and despite that he was penniless. Ridicule from his own colleagues, lack of recognition by the public, drove him into a life of depression and self-imposed exile. He started jotting down his theories and research activities in his diaries and notebooks instead of getting them published anywhere. It is absolutely ironical that the man who invented the modern world died a pauper in a lonely hotel room on January 7, 1943 at the age of 86. Half a century after his death, scientists are still trying to comprehend and study his various theories. Many of them are just now being proven. It is indeed sad that we never managed to recognize and appreciate a true genius like Tesla in his lifetime. But, now that you know all about him, you can make an endeavor to give Nikola Tesla his due credit, no matter belated it is.

Famous Quotes
“I dont care that they stole my idea . . I care that they dont have any of their own.”
“My brain is only a receiver, in the Universe there is a core from which we obtain knowledge, strength and inspiration. I have not penetrated into the secrets of this core, but I know that it exists.”
“The scientific man does not aim at an immediate result. He does not expect that his advanced ideas will be readily taken up. His work is like that of the planter – for the future. His duty is to lay the foundation for those who are to come, and point the way. He lives and labors and hopes.”
“I do not think there is any thrill that can go through the human heart like that felt by the inventor as he sees some creation of the brain unfolding to success . . . Such emotions make a man forget food, sleep, friends, love, everything.”
“The scientific man does not aim at an immediate result. He does not expect that his advanced ideas will be readily taken up. His work is like that of the planter—for the future. His duty is to lay the foundation for those who are to come, and point the way.”
“All that was great in the past was ridiculed, condemned, combated, suppressed — only to emerge all the more powerfully, all the more triumphantly from the struggle.”
11 Interesting fun facts about Nikola Tesla
Tesla suffered from insomnia and obsessive compulsive behavior (OCD).
Tesla was a genius in the true sense of the word; he could speak 8 languages and had the ability to memorize a large amount of information. You could ask him to recite any portion from anywhere from his book and he would have done it in a jiffy!
He was extremely fond of pigeons.
The International Unit of Magnetic Flux Density is called “Tesla” after him.
Tesla discovered X-ray radiation years before Roentgen was credited with its discovery.
Tesla had proposed to build a radio controlled boat to the U.S. military.
Though Tesla did not invent the light itself, he did find out the way to harness and distribute light over long distances.
He also predicted the internet by once saying: “The household’s daily newspaper will one day be printed ‘wirelessly’ in the home during the night”.
He claimed to have designed a death ray that could electrocute the enemy army from a distance of over 200 miles.
His work with electromagnetic waves resulted in the invention of the radio, radar and the MRI, a type of X-Ray that has enabled us to look inside the human body
During World War I, different countries were desperately looking for ways and means to detect enemy submarines under water. Tesla proposed the use of energy waves – the present day radar system technology – to detect the subs. However, the idea was rejected by all the scientists and military establishments as absurd and far-fetched. Sad, isn’t it? So, what happened thereafter? Well, the world then waited many more years for radars to be re-invented."""

tesla = tesla.lower()

f_disk = FreqDist

t_token = word_tokenize(tesla)
# print(t_token)
# print(stopwords.words('english'))

stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in t_token if not w.lower() in stop_words]

# print(filtered_sentence)

# for i in filtered_sentence:
#     print(i, " : ", lemmatizer.lemmatize(i))

for w in filtered_sentence:
    print(w, " : ", ps.stem(w))