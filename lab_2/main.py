"""
Longest common subsequence problem
"""

from tokenizer import tokenize

def tokenize_by_lines(text: str) -> tuple:
    """
    Splits a text into sentences, sentences – into tokens,
    converts the tokens into lowercase, removes punctuation
    :param text: the initial text
    :return: a list of sentences with lowercase tokens without punctuation
    e.g. text = 'I have a cat.\nHis name is Bruno'
    --> (('i', 'have', 'a', 'cat'), ('his', 'name', 'is', 'bruno'))
    """
    sent_list = []
    if not isinstance(text, str):
        return []
    new_text = ""
    text = text.lower()
    extra = set("""1234567890-=!@#$%^&*()_+,./<>?;:'"[{}]"'""")
    for c in text:
        if c not in extra:
            new_text += c
    new_text = new_text.split('\n')
    for sent in new_text:
        sent = tokenize(sent)
        if sent:
            sent_list.append(tuple(sent))

    return tuple(sent_list)


def create_zero_matrix(rows: int, columns: int) -> list:
    """
    Creates a matrix rows * columns where each element is zero
    :param rows: a number of rows
    :param columns: a number of columns
    :return: a matrix with 0s
    e.g. rows = 2, columns = 2
    --> [[0, 0], [0, 0]]
    """
    if not isinstance(rows,int) or not isinstance(columns,int):
        return []
    if str(type(rows)) == "<class 'bool'>" or str(type(columns)) == "<class 'bool'>":
        return []
    if rows == None or columns == None:
        return []
    if rows <= 0 or columns <= 0:
        return []
    return [[0 for j in range(columns)] for i in range(rows)]


def create_big_zero_matrix(rows, columns):

    return create_zero_matrix(rows + 1, columns + 1)


def fill_lcs_matrix(first_sentence_tokens: tuple, second_sentence_tokens: tuple) -> list:
    """
    Fills a longest common subsequence matrix using the Needleman–Wunsch algorithm
    :param first_sentence_tokens: a tuple of tokens
    :param second_sentence_tokens: a tuple of tokens
    :return: a lcs matrix
    """
    if not isinstance(first_sentence_tokens, tuple):
        return []

    if not isinstance(second_sentence_tokens,tuple):
        return []

    if not first_sentence_tokens:
        return []

    if not second_sentence_tokens:
         return []

    if str(type(first_sentence_tokens)) == "<class 'bool'>" or str(type(second_sentence_tokens)) == "<class 'bool'>":
        return []

    if first_sentence_tokens == None or second_sentence_tokens == None:
        return []

    for token in first_sentence_tokens:
        if not isinstance(token, str) and not isinstance(token, int):
            return []

        if str(type(token)) == "<class 'bool'>" or str(type(token)) == "<class 'bool'>":
            return []

        if token == None:
            return []

    for token in second_sentence_tokens:
        if not isinstance(token, str) and not isinstance(token, int):
            return []

        if str(type(token)) == "<class 'bool'>" or str(type(token)) == "<class 'bool'>":
            return []

        if token == None:
            return []


    LCS = create_big_zero_matrix(len(first_sentence_tokens), len(second_sentence_tokens))
    for i in range(len(first_sentence_tokens)):
        for j in range(len(second_sentence_tokens)):
            if first_sentence_tokens[i] == second_sentence_tokens[j]:
                LCS[i + 1][j + 1] = LCS[i][j] + 1
            else:
                LCS[i + 1][j + 1] = max(LCS[i][j + 1], LCS[i + 1][j])
    del LCS[0]

    for line in LCS:
        del line[0]

    return LCS


def find_lcs(first_sentence_tokens: tuple, second_sentence_tokens: tuple, lcs_matrix: list) -> tuple:
    """
    Finds the longest common subsequence itself using the Needleman–Wunsch algorithm
    :param first_sentence_tokens: a tuple of tokens
    :param second_sentence_tokens: a tuple of tokens
    :param lcs_matrix: a filled lcs matrix
    :return: the longest common subsequence
    """
    if not isinstance(first_sentence_tokens, tuple) or not isinstance(second_sentence_tokens, tuple)\
            or not isinstance(lcs_matrix, list)\
            or not len(first_sentence_tokens) == len(lcs_matrix) != 0\
            or lcs_matrix != fill_lcs_matrix(first_sentence_tokens, second_sentence_tokens):
        return ()


    if not lcs_matrix[0][0] in (0, 1) or len(lcs_matrix) != len(first_sentence_tokens) \
     or len(lcs_matrix[0]) != len(second_sentence_tokens):
        return ()


    for k in lcs_matrix:
        if not k:
            return ()
        if k == None:
            return ()
        if not isinstance(k,list):
            return ()
        for n in k:
            if not n:
                return ()
            if n == None:
                return ()
            if not isinstance(n,int):
                return ()
            if not str(type(n)) == "<class 'bool'>":
                return ()
            if n == None:
                return ()
            if n < 0:
                return ()


    i = len(lcs_matrix) - 1
    j = len(lcs_matrix[0]) - 1
    answer = []

    while i >= 1 and j >= 1:
        if first_sentence_tokens[i - 1] == second_sentence_tokens[j - 1]:
            answer.append(first_sentence_tokens[i - 1])
            i -= 1
            j -= 1
        else:
            if lcs_matrix[i - 1][j] > lcs_matrix[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return tuple(answer.__reversed__())


def find_lcs_length(first_sentence_tokens: tuple, second_sentence_tokens: tuple, plagiarism_threshold: float) -> int:
    """
    Finds a length of the longest common subsequence using the Needleman–Wunsch algorithm
    When a length is less than the threshold, it becomes 0
    :param first_sentence_tokens: a tuple of tokens
    :param second_sentence_tokens: a tuple of tokens
    :param plagiarism_threshold: a threshold
    :return: a length of the longest common subsequence
    """
    LCS = fill_lcs_matrix(first_sentence_tokens, second_sentence_tokens)

    if not isinstance(first_sentence_tokens, tuple) or not isinstance(second_sentence_tokens, tuple) or not isinstance(plagiarism_threshold, float):
        return -1

    if not first_sentence_tokens or not second_sentence_tokens or not plagiarism_threshold:
        return 0

    if not 0 <= plagiarism_threshold <= 1:
        return -1

    for token in first_sentence_tokens:
        if not isinstance(token, str) and not isinstance(token, int):
            return -1

    for token in second_sentence_tokens:
        if not isinstance(token, str) and not isinstance(token, int):
            return -1

    if len(LCS) / len(second_sentence_tokens) < plagiarism_threshold:
        return 0

    i = len(LCS) - 1
    j = len(LCS[0]) - 1
    return LCS[i][j]


def plagiarism(first_line: tuple, second_line: tuple) -> float:
    a = find_lcs_length(first_line, second_line, 0)
    res = calculate_plagiarism_score(a, second_line)
    return res


def calculate_plagiarism_score(lcs_length: int, suspicious_sentence_tokens: tuple) -> float:
    """
    Calculates the plagiarism score
    The score is the lcs length divided by the number of tokens in a suspicious sentence
    :param lcs_length: a length of the longest common subsequence
    :param suspicious_sentence_tokens: a tuple of tokens
    :return: a score from 0 to 1, where 0 means no plagiarism, 1 – the texts are the same
    """
    if not isinstance(suspicious_sentence_tokens, tuple):
        return -1

    for token in suspicious_sentence_tokens:
        if not isinstance(token, str):
            return -1

    if len(suspicious_sentence_tokens) == 0:
        return 0

    if not (0 <= lcs_length <= len(suspicious_sentence_tokens)):
        return -1

    plagiarism_score = lcs_length / len(suspicious_sentence_tokens)
    return plagiarism_score


def calculate_text_plagiarism_score(original_text_tokens: tuple, suspicious_text_tokens: tuple,
                                    plagiarism_threshold=0.3) -> float:
    """
    Calculates the plagiarism score: compares two texts line by line using lcs
    The score is the sum of lcs values for each pair divided by the number of tokens in suspicious text
    At the same time, a value of lcs is compared with a threshold (e.g. 0.3)
    :param original_text_tokens: a tuple of sentences with tokens
    :param suspicious_text_tokens: a tuple of sentences with tokens
    :param plagiarism_threshold: a threshold
    :return: a score from 0 to 1, where 0 means no plagiarism, 1 – the texts are the same
    """
    if not isinstance(original_text_tokens, tuple) or not original_text_tokens or not isinstance(suspicious_text_tokens, tuple) or not suspicious_text_tokens:
        return -1

    for i in original_text_tokens:
        if not isinstance(i, tuple):
            return -1
        for k in i:
            if not isinstance(k, str):
                return -1

    for i in suspicious_text_tokens:
        if not isinstance(i, tuple):
            return -1
        for k in i:
            if not isinstance(k, str):
                return -1


    sum = 0
    for lines in zip(original_text_tokens, suspicious_text_tokens):
        sum += plagiarism(lines[0], lines[1])
    return sum / len(suspicious_text_tokens)


def find_diff_in_sentence(original_sentence_tokens: tuple, suspicious_sentence_tokens: tuple, lcs: tuple) -> tuple:
    """
    Finds words not present in lcs.
    :param original_sentence_tokens: a tuple of tokens
    :param suspicious_sentence_tokens: a tuple of tokens
    :param lcs: a longest common subsequence
    :return: a tuple with tuples of indexes
    """
    og_sent = []
    sus_sent = []
    i = 0
    j = 0
    while i < len(original_sentence_tokens):
        if original_sentence_tokens[i] != lcs[j]:
            og_sent.append(i)
        else:
            j += 1
        i += 1

    i = 0
    j = 0

    while i < len(second_sentence_tokens):
        if second_sentence_tokens[i] != lcs[j]:
            sus_sent.append(i)
        else:
            j += 1
        i += 1
    return (tuple(og_sent), tuple(sus_sent))


def accumulate_diff_stats(original_text_tokens: tuple, suspicious_text_tokens: tuple, plagiarism_threshold=0.3) -> dict:
    """
    Accumulates the main statistics for pairs of sentences in texts:
            lcs_length, plagiarism_score and indexes of differences
    :param original_text_tokens: a tuple of sentences with tokens
    :param suspicious_text_tokens: a tuple of sentences with tokens
    :return: a dictionary of main statistics for each pair of sentences
    including average text plagiarism, sentence plagiarism for each sentence and lcs lengths for each sentence
    {'text_plagiarism': int,
     'sentence_plagiarism': list,
     'sentence_lcs_length': list,
     'difference_indexes': list}
    """
    # res_dict = {}
    #
    # text_plagiarism = calculate_text_plagiarism_score(original_text_tokens, suspicious_text_tokens, plagiarism_threshold=0.3)
    # res_dict["text_plagiarism"] = text_plagiarism
    # sentence_plagiarism = []
    # for lines in zip(original_text_tokens, suspicious_text_tokens):
    #     sentence_plagiarism.append(plagiarism(lines[0], lines[1]))
    # res_dict["sentence_plagiarism"] = sentence_plagiarism
    #
    # sentence_lcs_length = []
    # for lines in zip(original_text_tokens, suspicious_text_tokens):
    #     sentence_lcs_length.append(find_lcs_length(lines[0],lines[1]))
    # res_dict['sentence_lcs_length'] = sentence_lcs_length
    #
    # difference_indexes = []
    # for lines in zip(original_text_tokens, suspicious_text_tokens):
    #     difference_indexes.append(find_diff_in_sentence(lines[0],lines[1]))
    # res_dict[difference_indexes] = difference_indexes
    pass

def create_diff_report(original_text_tokens: tuple, suspicious_text_tokens: tuple, accumulated_diff_stats: dict) -> str:
    """
    Creates a diff report for two texts comparing them line by line
    :param original_text_tokens: a tuple of sentences with tokens
    :param suspicious_text_tokens: a tuple of sentences with tokens
    :param accumulated_diff_stats: a dictionary with statistics for each pair of sentences
    :return: a report
    """
    pass


def find_lcs_length_optimized(first_sentence_tokens: list, second_sentence_tokens: list) -> int:
    """
    Finds a length of the longest common subsequence using the Hirschberg's algorithm
    At the same time, if the first and last tokens coincide,
    they are immediately added to lcs and not analyzed
    :param first_sentence_tokens: a list of tokens
    :param second_sentence_tokens: a list of tokens
    :return: a length of the longest common subsequence
    """
    pass
