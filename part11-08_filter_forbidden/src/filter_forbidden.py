# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    filtered = "".join([char for char in string if char not in forbidden])
    return filtered

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)