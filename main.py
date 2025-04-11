# main.py
import stats
import sys
import os


def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The contents of the file, or an error message if reading fails.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File not found at '{filepath}'"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Reads a book from a file, analyzes its word and character counts,
    and prints the results.
    """
    # Ensure the 'books' directory exists in the same location as main.py
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = sys.argv[1]
    book_content = get_book_text(filepath)

    if isinstance(book_content, str) and not book_content.startswith("Error"):
        word_count = stats.count_words(book_content)
        print(f'Found {word_count} total words')
        print("-" * 30)

        character_counts = stats.repeat_characters(book_content)
        print("Character Counts (Unsorted):")
        for char, count in character_counts.items():
            print(f"{char}: {count}")
        print("-" * 30)

        sorted_character_list = stats.sort_character_counts(character_counts)
        print("Character Counts (Sorted Alphabetically):")
        for item in sorted_character_list:
            print(f"'{item['character']}': {item['count']}")
    else:
        print(book_content)

if __name__ == "__main__":
    main()