from collections import Counter
def count_words(sentence:str)-> dict:
    if not isinstance(sentence,str):
        raise TypeError("Đầu vào phải là một chuỗi")
    return dict(Counter(sentence.lower().split()))
print(count_words(""))
