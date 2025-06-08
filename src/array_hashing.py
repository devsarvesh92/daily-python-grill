



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

def top_k_frequent_elements(*,nums:list[int],k:int)->list[int]:
    d:dict[int,int] = defaultdict(int)

    for i in nums:
        d[i]+=1
    
    sd:dict[int,int] = dict(sorted(d.items(),key=lambda k:k[1],reverse=True))
    return list(sd.values())[:k]


