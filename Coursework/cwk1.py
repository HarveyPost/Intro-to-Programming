"""
Introduction to Programming Coursework 1

@author: sc23hp2
"""


def valid_puzzle(puzzle: list) -> bool:
    # Check if puzzle is a list of strings with at least 2 strings
    if not isinstance(puzzle, list) or len(puzzle) < 2:
        return False
    for i in puzzle:
        # Check if each string is a string, is the same length as the first, and is alphabetical
        if not isinstance(i, str):
            return False
        if len(i) != len(puzzle[0]):
            return False
        if not i.isalpha():
            return False
    return True


def similarity_grouping(data: list) -> list:
    groups = []
    for i in data:
        found = False
        # Iterate through each group, if i is in the group, add it to the group
        for group in groups:
            if i in group:
                group.append(i)
                found = True
                break
        # If i is not in any group, create a new group with i in it
        if not found:
            groups.append([i])
    return groups


def highest_count_items(data: str) -> list:
    # Return an emptpy list if data is not a string
    if not isinstance(data, str):
        return []
    items = data.split(',')
    # Create a dictionary of items and their counts
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    max_count = max(count.values())
    # Return a list of items with the highest count
    result = [[item, value] for item, value in count.items() if value == max_count]
    return result


def valid_char_in_string(popList: list, charSet: list) -> bool:
    # Check if popList and charSet are lists
    if not isinstance(popList, list) or not isinstance(charSet, list):
        return False
    # Create a shallow copy of charSet
    valid_chars = charSet[:]
    # Iterate through each character in each list and check if it is in charSet
    for string in popList:
        for char in string:
            if char not in valid_chars:
                return False
    return True


def total_price(unit: int) -> float:
    if unit < 6:
        price = unit * 1.25
        return price
    elif unit % 6 == 0:
        price = (unit / 6) * 5
        # Check if price is over 20, if so apply discount
        if price > 20:
            price = price * 0.9
            return price
        else:
            return price
    else:
        price = (unit // 6) * 5 + (unit % 6) * 1.25
        if price > 20:
            price = price * 0.9
            return price
        else:
            return price



if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
