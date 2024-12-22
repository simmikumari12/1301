import sys

def song_dic(filename):
    with open(filename, 'r') as file:
        lyrics = []
        for line in file:
            lyrics.append(line.strip())
    
    position_of_words = {}
    line_number = 1
    
    # Track word positions for each line in the song
    for line in lyrics:
        words = line.strip().split()
        for index, word in enumerate(words, start=1):
            word = word.upper()  # Convert to uppercase to keep consistent word tracking
            if word not in position_of_words:
                position_of_words[word] = []
            
            # Track positions for each word
            position_of_words[word].append(line_number)  # Record the line number of the word
            
        line_number += 1  # Increment line number
    
    # Print the dictionary of word positions
    print("\nDictionary:\n")
    for word, positions in sorted(position_of_words.items()):
        print(f"{word.ljust(10)} {positions}")

    # Reconstruct the song lyrics line by line
    reconstructed_lyrics = []
    for line_number in range(1, len(lyrics) + 1):
        reconstructed_line = []
        words_in_line = lyrics[line_number - 1].split() 
        print(words_in_line)

        # For each word in the original line, check if it appears in the current line's position
        for word in words_in_line:
            word_upper = word.upper()  # Convert to uppercase to match
            if line_number in position_of_words[word_upper]:  # Ensure the word belongs to this line
                reconstructed_line.append(word_upper)
        
        # Join the reconstructed words to form the complete line
        reconstructed_lyrics.append(" ".join(reconstructed_line))
    
    # Print the reconstructed song lyrics
    print("\nSong:\n")
    for line in reconstructed_lyrics:
        print(line)
        
    # Print the unique word count and the most frequent word(s)
    unique_words_count = len(position_of_words)
    print(f"\nThe number of unique words in the lyric are: {unique_words_count}\n")
    
    word_frequencies = {word: len(positions) for word, positions in position_of_words.items()}
    max_frequency = max(word_frequencies.values())
    most_frequent_words = [word for word, freq in word_frequencies.items() if freq == max_frequency]
    print(f"Most frequent word(s): {', '.join(most_frequent_words)}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python SongLyrics.py <song_file>")
        sys.exit(1)
    song_file = sys.argv[1]
    song_dic(song_file)

if __name__ == "__main__":
    main()
