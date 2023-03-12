# Import the Spacy library
import spacy

# Load the medium-sized English model of Spacy
nlp = spacy.load('en_core_web_md')

# Define a function that takes in a description and returns the title of the most similar movie
def get_most_similar_movie(description):
    # Open the movies.txt file
    with open('movies.txt', 'r') as f:
        # Read in each line of the file
        lines = f.readlines()

    # Initialize variables to keep track of the maximum similarity and the most similar movie
    max_similarity = -1
    most_similar_movie = ''

    # Iterate over each line in the file
    for line in lines:
        # Split the line into the movie title and description
        movie_title, movie_description = line.split(':', 1)
        # Compute the similarity between the given description and the movie description using Spacy
        similarity = nlp(description).similarity(nlp(movie_description))
        # If the similarity is greater than the current maximum, update the maximum and most similar movie
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie_title.strip()

    # Return the title of the most similar movie
    return most_similar_movie

# If this script is being run directly, test it by calling the function with a sample description
if __name__ == '__main__':
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    print(get_most_similar_movie(description))

