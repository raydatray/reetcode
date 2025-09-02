"""
https://leetcode.com/problems/text-justification/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

from typing import List


class Solution:
    def full_justify(self, words: List[str], max_width: int) -> List[str]:
        result = []

        curr_line = []
        curr_char_count = 0

        for word in words:
            if curr_char_count + len(word) + len(curr_line) > max_width:
                if len(curr_line) == 1:
                    line = curr_line[0] + " " * (max_width - len(curr_line[0]))
                else:
                    remaining_space = max_width - curr_char_count
                    spaces = remaining_space // (len(curr_line) - 1)
                    extra_spaces = remaining_space % (len(curr_line) - 1)

                    line = ""
                    for i, w in enumerate(curr_line):
                        line += w
                        if i < len(curr_line) - 1:
                            line += " " * spaces
                            if extra_spaces > 0:
                                line += " "
                                extra_spaces -= 1

                result.append(line)

                curr_line = [word]
                curr_char_count = len(word)
            else:
                curr_line.append(word)
                curr_char_count += len(word)

        last_line = " ".join(curr_line)
        last_line += " " * (max_width - len(last_line))
        result.append(last_line)

        return result


def test_one():
    solution = Solution()
    result = solution.full_justify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    )

    assert result == ["This    is    an", "example  of text", "justification.  "]


def test_two():
    solution = Solution()
    result = solution.full_justify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16
    )

    assert result == ["What   must   be", "acknowledgment  ", "shall be        "]


def test_three():
    solution = Solution()
    result = solution.full_justify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )

    assert result == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
