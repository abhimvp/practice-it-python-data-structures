import string
from collections import Counter
paragraph = """Nadia’s Garden Restaurant is the creation of husband and wife team Nadia and Timothy Arbore. 
    Their American-infused, Italian-based, organically created, cuisine was inspired by Nadia’s papa, an immigrant from Italy, 
    who shared his love of cooking with Nadia as a young girl. His focus on using fresh ingredients and family style dining were 
    the inspiration for Nadia’s Garden Restaurant. Located in the heart of Main Streets Historic District, they are proud to be a 
    part of a rich community. In 2011, the duo remodeled the restaurant and updated their menu to include newer and more diverse entrées
     that could be made from local organic suppliers. Preservation of the building’s original layout has allowed them to create smaller, 
     more intimate, dining spaces. Nadia and Timothy are committed to sharing their family history of cuisine, along with their new inspirations,
      with their customers. Their passion for community, entertainment, and hospitality are found in every aspect of Nadia’s Garden Restaurant."""

paragraph=paragraph.lower()
# string.punctuation is a pre-defined string within the string module in Python. It contains a collection of all common punctuation characters,
# including: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
# The line paragraph.translate(str.maketrans('','',string.punctuation)) specifically does this:
# Creates a Mapping: str.maketrans('','',string.punctuation) builds a translation table where each punctuation character from string.punctuation is mapped to None (essentially, it tells Python to delete these characters).
# Translates the Paragraph:  The paragraph.translate() function applies this mapping. Any time it
# encounters a punctuation character from string.punctuation within your paragraph string, it removes it.
paragraph=paragraph.translate(str.maketrans('','',string.punctuation))
wordList = paragraph.split() #splits the words and forms an array of words
print(len(wordList)) # or
counter = Counter(wordList)
print("the no.of words in a paragraph are ", counter)
