#   This program makes a movie viewing recommendation using NLP

# import spacy and natural language processing model.
import spacy
nlp = spacy.load('en_core_web_md')


def watch_next(movie):
    # opens movies.txt file
    movies = open("movies.txt")
    # split movie title and description
    movies_split = []

    # split movies into title and description and store in list
    for i in movies:
        movies_split.append(i.split(':'))

    # get number of movies in text file
    movie_total = len(movies_split)
    # create list to store similarities
    movie_similarities = []

    previous_movie = nlp(movie)

    # iterate through movie list
    for i in range(0, movie_total):
        # get similarities for films in list and Planet Hulk
        movie_similarities.append(nlp(movies_split[i][1]).similarity(previous_movie))
    # find max similarity value
    max_similarity = max(movie_similarities)
    # get index of most similar movie to Planet Hulk
    index_max_similarity = movie_similarities.index(max_similarity)

    # return movie title from index
    return movies_split[index_max_similarity][0]


# description of Planet Hulk
planet_hulk = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space 
to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold
into slavery and trained as a gladiator."""

# prints off most similar film to Planet Hulk
print(f"\nBased on your recent viewing,\nWe think you'll like:\n{watch_next(planet_hulk)}")
