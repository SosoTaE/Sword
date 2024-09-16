import string


def get_georgian_words(text):
  """
  Extracts Georgian words from the provided text.

  Args:
      text: The text to process.

  Returns:
      A list of Georgian words found in the text.
  """

  # Define the Georgian alphabet characters
  georgian_alphabet = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"

  # Remove punctuation and split the text into words
  translator = str.maketrans('', '', string.punctuation)
  words = text.translate(translator).split()

  # Filter out non-Georgian words
  georgian_words = [word for word in words if all(char in georgian_alphabet for char in word)]

  return georgian_words


def contains_only_georgian_letters(word):
    """
    Checks if a word contains only Georgian letters.

    Args:
        word (tr): The word to check.

    Returns:
        bool: True if the word contains only Georgian letters, False otherwise.
    """

    georgian_alphabet = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
    return all(letter in georgian_alphabet for letter in word)

