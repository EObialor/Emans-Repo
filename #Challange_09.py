#Challange_09

text = ''' 


In the whimsical realm of flibbering floofs and wibbly-wobbly widgets, the zippity-zap squirrels play tag with rainbow-hued fireflies.
Meanwhile, a troupe of polka-dotted penguins tap dance atop towering stacks of pancakes,
serenading the moon with jazzy tunes that make the stars shimmy in the velvety night sky.
Unicorns in top hats and monocles sip chamomile tea and discuss the finer points of quantum quokka mechanics,
while a friendly, three-headed, spacefaring snail named Gerald offers intergalactic wisdom to all who pass by.
In the enchanted forest of snicker-snacking Snickerdoodles, jellybean bushes hum sweet lullabies to the marshmallow mushrooms,
who, in turn, tell stories of marshmallow mushroom adventures in far-off gumdrop valleys.
A mischievous lemonade rain shower occasionally descends, turning the ground into fizzy, 
zesty streams that bubble and fizz their way to the cotton candy coastline. On the horizon,
a colossal, ice cream sundae mountain stands tall, 
where brave explorers can scale its whipped cream peaks and discover treasure troves of caramel 
rivers and chocolate coin caves. Meanwhile, in the heart of this sugar-coated wonderland, 
the Tickle-Me-Elmo trees giggle uncontrollably,
spreading joy to all who venture into this delightful dreamscape.


'''

import re

# function to count the words
def count_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Function to show repeating words in table
def display_word_frequencies(word_count):
    print(f"{'Word':<20} {'Frequency':<10}")
    print("-" * 30)
    for word, count in sorted(word_count.items()):
        print(f"{word:<20} {count:<10}")


if __name__ == "__main__":
    word_frequencies = count_word_frequencies(text)
    display_word_frequencies(word_frequencies)
