# Given a string as input, return the list of all the patterns possible:
#
#
# '1' : ['A', 'B', 'C'],
# '2' : ['D', 'E'],
# '12' : ['X']
# '3' : ['P', 'Q']
# Example if input is '123', then output should be [ADP, ADQ, AEP, AEQ, BDP, BDQ, BEP, BEQ, CDP, CDQ, CEP, CEQ, XP, XQ]
#

# Q: are we looking for combinations, or permutations? (Looks like combinations.)
# Q: if the number is there twice, do we double the letters? (no)

from itertools import combinations

def string_combos(input_string):
    d = {
        '1' : ['A', 'B', 'C'],
        '2' : ['D', 'E'],
        '12' : ['X'],
        '3' : ['P', 'Q']
    }
    strs = detect_strings(input_string, d)
    patterns = get_combinations(strs)
    return patterns

def detect_inputs(input_string, d):
    '''return list of possible patterns'''
    strings_list = []
    pass

def get_combinations(strs):
    pass




# From career cup page:

def get_patterns(digit, s=0):
	values = {'1': ['A', 'B', 'C'],
			  '2': ['D', 'E'],
			  '12': ['X'],
			  '3': ['P', 'Q']}

	if s == len(digit)-1:
		return values.get(digit[s], [])

	res = list()
	for i in range(s, len(digit)-1):
		sub_p = get_patterns(digit, i+1)
		for l1 in sub_p:
			for l2 in values.get(digit[s:i+1], []):
				res.append(l2+l1)
	return res

print(get_patterns('123'))


# And another example

input_str = '123'
# input_str = '1'

d = {
    '1' : ['A', 'B', 'C'],
    '2' : ['D', 'E'],
    '12' : ['X'],
    '3' : ['P', 'Q']
}

def permute(res_str, in_str):
    if in_str == '':
        print(res_str)
        return
#     get letter or multiple of them
    for i in range(1, len(in_str)+1):
        key = in_str[:i]
        if key in d:
            # print('key found', key)
            for item in d[key]:
                permute(res_str + item, in_str[i:])

permute(res_str='',in_str=input_str)
