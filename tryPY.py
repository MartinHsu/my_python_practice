c_ranks = {'ghost': 1, 'habanero': 2, 'cayenne':3}
rank_dict = {rank: name for name, rank in c_ranks.items()}
c_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(c_len_set)