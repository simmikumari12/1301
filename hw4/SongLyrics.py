import sys
def song_dic(filename):
    with open(filename, 'r') as file:
        lyrics = []
        for line in file:
            lyrics.append(line.strip())
    position_of_words = {}
    word_position = 1
    line_number =1
    for line in lyrics:
        words = line.strip().split()
        for index, word in enumerate(words, start=1):
            word = word.upper() 
            if word not in position_of_words:
                position_of_words[word] = []
            if index == len(words):
                position_of_words[word].append(-word_position)
            else:
                position_of_words[word].append(word_position)
            word_position = word_position + 1
        line_number += 1
    print("\nDictionary:\n")
    for word, positions in sorted(position_of_words.items()):
        print(f"{word.ljust(10)} {positions}")

    print("\nSong:\n")
    for line_number in range(1, len(lyrics) + 1):
        words_in_line = lyrics[line_number - 1].split()
        song_list_in_uppercase =[]
      
        for word in words_in_line:
            word_upper = word.upper() 
            song_list_in_uppercase.append(word_upper)
        song_line = " ".join(song_list_in_uppercase)
        print(song_line)
      
    unique_words_count = len(position_of_words)
    print(f"\nThe number of unique words in the lyric are: {unique_words_count}\n")
    word_frequencies = {word: len(positions) for word, positions in position_of_words.items()}
    max_frequency = max(word_frequencies.values())
    most_frequent_words = [word for word, freq in word_frequencies.items() if freq == max_frequency]
    print(f"Most frequent word(s): {', '.join(most_frequent_words)}\n")

def main():
    if len(sys.argv) != 2:
        print("Please give two Command Line Argument!")
        sys.exit(1)
    song_file = sys.argv[1]
    song_dic(song_file)

if __name__ == "__main__":
    main()

