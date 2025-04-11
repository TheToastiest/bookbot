# stats.py

def count_words(text):
    """
    Counts the number of words in a given string.

    Args:
        text (str): The input string.

    Returns:
        int: The number of words in the string.
    """
    words = text.split()
    return len(words)

def repeat_characters(text):
    """
    Counts the number of times each character appears in a string (case-insensitive).

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary where keys are lowercase characters and values are their counts.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries
    using the .sort() method.

    Args:
        char_counts (dict): A dictionary where keys are characters and values are their counts.

    Returns:
        list: A list of dictionaries, each with 'character' and 'count' keys,
              sorted alphabetically by character.
    """
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({'character': char, 'count': count})

    # Sort the list of dictionaries in-place using the .sort() method
    sorted_list.sort(key=lambda item: item['character'])

    return sorted_list