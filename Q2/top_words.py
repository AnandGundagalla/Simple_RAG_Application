import re
from collections import Counter

def get_top_words(file_path, top_n=5):
    stopwords = {
        "the","is","in","and","to","of","a","for","on","with",
        "at","by","an","be","this","that","it","as","are","was"
    }

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()

    text = re.sub(r"[^\w\s]", " ", text)
    words = text.split()
    words = [word for word in words if word not in stopwords]

    count = Counter(words)
    return count.most_common(top_n)


if __name__ == "__main__":
    result = get_top_words("sample.txt")
    print(result)
