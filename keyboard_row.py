
"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:


        all_keys = ["qwertyuiop","asdfghjkl","zxcvbnm"]

        valid_keyboard_words = []

        # iterate over word list
        for word in words: 

            valid_word = True
            lower_word = word.lower()
            first_char = lower_word[0]
            keyboard_idx = {}

            # iterate over all keyboard row list to determine which row to use
            for row_keys in all_keys:

                if first_char in row_keys:

                    keyboard_idx = row_keys

            # iterate over each character to check if its a keyboard row list
            for i in lower_word:

                if i not in keyboard_idx:

                    valid_word = False
                    break
            if valid_word:

                valid_keyboard_words.append(word)

        return valid_keyboard_words