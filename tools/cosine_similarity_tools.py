import numpy as np
def calculate_cosine_similarity(vector1, vector2):
    """
    Calculates the cosine similarity between two vectors.

    Args:
        vector1 (numpy.ndarray): The first vector.
        vector2 (numpy.ndarray): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """

    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)

    similarity = dot_product / (norm_vector1 * norm_vector2)

    return similarity

def compare_words_char_cosine_similarity(word1, word2):
    """
    Compares two words using cosine similarity based on their character-level representations.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        float: The cosine similarity between the two words (between 0 and 1).
    """

    # Create a set of all unique characters from both words
    all_chars = set(word1).union(set(word2))

    # Create vectors representing character counts
    vector1 = np.array([word1.count(char) for char in all_chars])
    vector2 = np.array([word2.count(char) for char in all_chars])

    # Calculate dot product
    dot_product = np.dot(vector1, vector2)

    # Calculate magnitudes (norms) of the vectors
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Calculate cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        # Handle cases where one or both words are empty
        return 0.0
    else:
        similarity = dot_product / (magnitude1 * magnitude2)
        return similarity


def compare_words(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    tokens = word1 + word2

    word1_vector = []
    for each in tokens:
        if each in word1:
            word1_vector.append(1)
        else:
            word1_vector.append(0)

    word2_vector = []
    for each in tokens:
        if each in word2:
            word2_vector.append(1)
        else:
            word2_vector.append(0)

    point = 0

    for i in range(len(tokens)):
        if word1_vector[i] == word2_vector[i]:
            point += 1

    return point / len(tokens)