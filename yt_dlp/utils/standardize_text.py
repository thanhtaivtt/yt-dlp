import re


def remove_emoji(text):
    if text is None:
        return text

    emoji_pattern = re.compile('['
                               '\U0001F600-\U0001F64F'  # Emoticons
                               '\U0001F300-\U0001F5FF'  # Symbols & Pictographs
                               '\U0001F680-\U0001F6FF'  # Transport & Map Symbols
                               '\U0001F700-\U0001F77F'  # Alchemical Symbols
                               '\U0001F780-\U0001F7FF'  # Geometric Shapes
                               '\U0001F800-\U0001F8FF'  # Supplemental Arrows-C
                               '\U0001F900-\U0001F9FF'  # Supplemental Symbols and Pictographs
                               '\U0001FA00-\U0001FA6F'  # Chess Symbols, etc.
                               '\U0001FA70-\U0001FAFF'  # More pictographs
                               '\U00002702-\U000027B0'  # Dingbats
                               '\U000024C2-\U0001F251'  # Enclosed Characters
                               ']+', flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def remove_special_chars(text):
    if text is None:
        return text

    return re.sub(r'[.,\'"#]', '', text)  # Removes ., ', ", and #


def standardize_text(text):
    return remove_special_chars(remove_emoji(text))


class StandardizeText:
    def __init__(self, text):
        self.text = text

    def standardize(self):
        return standardize_text(self.text)
