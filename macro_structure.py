import random
from functools import reduce

def get_duration(paragraph, average, minimum, maximum):
    while True:
        if isinstance(average, int):
            list = [random.randint(minimum, maximum) for i in range(paragraph)]
        if isinstance(average, float):
            list = [round(random.uniform(minimum, maximum), 1) for i in range(paragraph)]
            # print(list)
        current_average = reduce(lambda x, y: x + y, list) / len(list)
        if current_average == average:
            return list

def glue_list(intro_outro, section_list):
    glued_list = []
    for i in range(len(intro_outro + section_list)):
        if i == 0:
            glued_list.append(intro_outro[0]); continue
        if i == len(intro_outro + section_list) - 1:
            glued_list.append(intro_outro[-1]); break
        else:
            glued_list.append(section_list[i-1]); continue
    return glued_list

def sec_convertor(glued_list):
    sec_list = []
    for i in range(len(glued_list)):
        sec_list.append(int(glued_list[i] * 60))
    return sec_list

def section_namer(intro_outro, section_list):
    name_list = []
    intro_name, section_name = ['intro', 'outro'], ['A', 'B', 'C', 'D']
    list_length = len(intro_outro + section_list)
    for i in range(list_length):
        if i == 0:
            name_list.append(intro_name[0]); continue
        if i == 1:
            value = random.choice(['A', 'B'])
            name_list.append(value); prev = value; continue
        if 2 <= i <= list_length - 2:
            while True: 
                value = random.choice(section_name)
                if value != prev:
                    name_list.append(value); prev = value; break
        if i == list_length - 1:
            name_list.append(intro_name[-1]); break
    return name_list

def get_section(piece_list):
    total_min, total_name, total_sec = [], [], []
    for number in piece_list:
        intro_outro = get_duration(2, number*0.05, number*0.03, number*0.1)
        # print(intro_outro, str(len(intro_outro)))
        sec_num = random.randint(5, 8); sec_avg = round(number * 0.9 / sec_num, 1)
        sec_min, sec_max = round(sec_avg * 0.5, 1), round(sec_avg * 2, 1)
        section_list = get_duration(sec_num, sec_avg, sec_min, sec_max)
        # print(section_list, str(len(section_list)))

        glued_list = glue_list(intro_outro, section_list); print(glued_list, str(len(glued_list)))
        total_min.append(glued_list)

        name_list = section_namer(intro_outro, section_list); print(name_list, str(len(name_list)))
        total_name.append(name_list)

        sec_list = sec_convertor(glued_list); print(sec_list, str(len(sec_list)), '\n')
        total_sec.append(sec_list)
    return total_min, total_name, total_sec

if __name__ == '__main__':
    paragraph = random.randint(5, 8)
    print('\nparagraph:', str(paragraph))
    piece_list = get_duration(paragraph, 10, 8, 12)
    print('piece_list:', str(piece_list), str(sum(piece_list)), '\n')
    section = get_section(piece_list)
    print('total_min:', section[0], len(section[0]),'\n')
    print('total_name:', section[1], len(section[1]),'\n')
    print('total_sec:', section[2], len(section[2]))