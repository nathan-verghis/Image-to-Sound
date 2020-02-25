import timeit


def create_colour_index():
    colour_index = {}
    i = 0
    for r in range(256):
        for g in range(256):
            for b in range(256):
                colour_index[i] = (r, g, b)
                i += 1
    return colour_index


color_index = create_colour_index()
for i in color_index:
    if color_index[i] == (255, 255, 255):
        print(color_index[i])

'''


code_to_test = """
color_index = create_colour_index()
for i in color_index:
    if color_index[i] == (255, 255, 255):
        print(color_index[i])
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)'''
