# python -i file.py
# from file import *
walls = {
1: [],
2: [12],
3: [13],
4: [14],
5: [6],
6: [5],
7: [17],
8: [18],
9: [],
10: [],
11: [12],
12: [11,2,22],
13: [3,23],
14: [4,24],
15: [16,25],
16: [15,17],
17: [7,16],
18: [7,16],
19: [29],
20: [30],
21: [],
22: [12,32],
23: [13,33],
24: [14,34],
25: [15,35],
26: [27],
27: [26,37,28],
28: [27],
29: [19,39],
30: [20],
31: [41],
32: [42],
33: [43],
34: [35],
35: [34,45],
36: [46],
37: [47],
38: [39,48],
39: [29,38,40],
40: [39],
41: [31],
42: [32,43,52],
43: [33],
44: [45],
45: [44,35],
46: [36,56],
47: [37,57],
48: [38,58],
49: [50,59],
50: [49,60],
51: [61],
52: [42,62],
53: [54],
55: [65],
56: [46,66],
57: [47,67],
58: [48,68],
59: [49,69],
60: [50],
61: [51],
62: [52,72],
63: [64,73],
64: [63,65],
65: [55,64,75],
66: [56],
67: [57,68],
68: [58,67],
69: [59,79],
70: [80],
71: [],
72: [62],
73: [63,83],
74: [84],
75: [65],
76: [77],
77: [76,78],
78: [77,88],
79: [69,89],
80: [70],
81: [82],
82: [81,83],
83: [73,82,93],
84: [74,85,94],
85: [84,86],
86: [85,87],
87: [86,97],
88: [78,98],
89: [79,99],
90: [],
91: [92],
92: [91],
93: [83],
94: [84],
95: [85],
95: [96],
96: [95],
97: [87],
98: [88],
99: [89],
100: []
}


# '00': leste,
# '01': norte,
# '10': oeste,
# '11': sul

move_value = {
'00': +1,
'01': -10,
'10': -1,
'11': +10
}

def move_truck(current,direction):
    new = current + move_value[direction]
    if new < 0 or new > 100:
        result = 'Fora do mapa'
    elif current % 10 == 0 and direction == '00':
        result = 'Fora do mapa'
    elif current % 10 == 1 and direction == '10':
        result = 'Fora do mapa'
    elif new in walls[current]:
        result = 'Parede'
    else:
        result = 'OK'
        print(f"{current} -> {new} : {result}")
        return new

cromossomo = "0101010000011010010000000000000000000101010100"

def show_track(cromossomo):
    current = 91
    start = 0
    end = 2
    for i in range(23):
        current = move_truck(current,cromossomo[start:end])
        start += 2
        end += 2

show_track(cromossomo)
