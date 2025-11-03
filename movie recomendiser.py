import random
from textblob import TextBlob
movies = [
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "overview": "A skilled thief enters dreams to steal secrets but must plant an idea instead."
    },
    {
        "title": "The Lion King",
        "genre": "Animation",
        "rating": 8.5,
        "overview": "A young lion prince flees after his father's death and learns the true meaning of bravery."
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "rating": 8.4,
        "overview": "The Avengers assemble to undo the catastrophic events by Thanos."
    }
]

movie = random.choice(movies)
analysis = TextBlob(movie["overview"]).sentiment.polarity
sentiment = "Positive" if analysis > 0 else "Negative"

print("Random Movie Recommendation")
print("---------------------------")
print("Title:", movie["title"])
print("Genre:", movie["genre"])
print("IMDB Rating:", movie["rating"])
print("Overview:", movie["overview"])
print("Sentiment:", sentiment)
