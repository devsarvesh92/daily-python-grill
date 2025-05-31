



from collections import defaultdict


def group_anagrams(*,input:list[str])->list[list[str]]:
    """
    Group anagrams

    :param input
    :type input: list[str]

    :return: grouped anagrams
    :rtype:list[list[str]]
    """
    gp = defaultdict(list)

    for ip in input:
        gp["".join(sorted(ip))].append(ip)

    
    return [v for k,v in gp.items()]