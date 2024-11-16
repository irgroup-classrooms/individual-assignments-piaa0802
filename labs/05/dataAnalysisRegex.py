import csv
import re
from collections import Counter

def main():

    with open('C:/Uni/DIS08/individual-assignments-piaa0802/labs/05/lotr-scripts-csv.csv', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        rows = list(reader)  # Convert to a list of dictionaries

    # Extract columns into separate lists
    dialogs = [row['dialog'] for row in rows]
    chars = [row['char'] for row in rows]
    movies = [row['movie'] for row in rows]

    # Task 1: Total number of lines and unique words in the dialogues
    total_lines = len(dialogs)  # Total number of lines
    all_dialogues = " ".join(dialogs)  # Combine all dialogues
    unique_words = set(re.findall(r'\b\w+\b', all_dialogues))  # Extract unique words

    # Task 2: Distribution of lines across the three films
    film_distribution = Counter(movies)

    # Task 3: Top 5 characters in the char column
    top_chars = Counter(chars).most_common(5)

    # Task 4: Top 5 characters mentioned in the dialogues
    words_in_dialogues = re.findall(r'\b\w+\b', all_dialogues)
    mentioned_chars = Counter(word.upper() for word in words_in_dialogues)
    # Filter for characters mentioned in the dialogues that are in the char column
    unique_chars = set(char.upper() for char in chars)
    top_mentioned_chars = [
        (char, count) for char, count in mentioned_chars.items() if char in unique_chars
    ]
    top_mentioned_chars = sorted(top_mentioned_chars, key=lambda x: -x[1])[:5]

    # Output the results
    #return total_lines, len(unique_words), film_distribution, top_chars, top_mentioned_chars
    print("Total number of lines used in the dialogs: ", total_lines)
    print("Totel number of unique words used in the dialogs: ",len(unique_words))
    print("Distribution of lines on the three diferrent films: ",film_distribution)
    print("Top 5 characters in the char column: ",top_chars)
    print("Top 5 characters in the dialogues: ",top_mentioned_chars)

if __name__ == '__main__':
    results = main()
    print(results)