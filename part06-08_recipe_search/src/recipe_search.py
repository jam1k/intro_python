# Write your solution here

def reading_file(filename):
    names = []
    with open(filename) as f:
        names.append(f[0])
        for line in f:
            if line == "\n":
                continue
            
    

def search_by_name(filename: str, word: str):
    receipes = reading_file("/Users/jamilya/Library/Application Support/tmc/vscode/mooc-programming-22/part06-08_recipe_search/src/recipes1.txt")

    result
    for receipe