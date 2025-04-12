def how_many_words(contents):
    return len(contents.split())


def count_chars(contents):
    lower_contents = contents.lower()
    unique_chars = set(lower_contents)
    counted_chars = {char: lower_contents.count(char) for char in unique_chars}
    return counted_chars


def sort_counted_chars(counted_chars):
    chars_list = [
        {"char": char, "count": count} for char, count in counted_chars.items()
    ]
    chars_list.sort(reverse=True, key=lambda char_dict: char_dict["count"])
    return chars_list
