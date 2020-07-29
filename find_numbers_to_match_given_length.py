# Write a function that takes an integer flight_length (in minutes) and a list of integers 
# movie_lengths (in minutes) and returns a boolean indicating whether 
# there are two numbers in movie_lengths whose sum equals flight_length.

# When building your function:

# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory


def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False
    
    
# Complexity:
# O(n) time, and 
# O(n) space. 
# Note while optimizing runtime we added a bit of space cost.

# What We Learned
# The trick was to use a set to access our movies by length, in O(1) time.

# Using hash-based data structures, like dictionaries or sets, is so common in coding challenge solutions,
# it should always be your first thought. Always ask yourself, right from the start: "Can I save time by using a dictionary?"
