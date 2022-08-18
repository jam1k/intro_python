# Write your solution here
import fnmatch
def reading_file(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def return_asteriks_index(search_term):
    return [i for i in range(len(search_term)) if search_term.startswith('*', i)]

def return_dot_index(search_term):
    return [i for i in range(len(search_term)) if search_term.startswith('.', i)]

def find_words(search_term: str):
    words = reading_file("words.txt")
    search_term = search_term.replace(".", "?")
    filtered = fnmatch.filter(words, search_term)
    return filtered

if __name__ == "__main__":
    print(find_words("ca."))