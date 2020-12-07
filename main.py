with open("input.txt") as file:
    data = file.read().split('\n')


def line_to_dict(line):
    split_two = line.split(" contain")
    main_bag = split_two[0].replace(" bags","")
    inside_bags = split_two[1].split(",")
    return {main_bag: inside_bags}


all_the_bags = {}


for d in data:
    all_the_bags.update(line_to_dict(d))


def get_substitute_colors(base_color_in_list):

    new_color = False

    for key in all_the_bags:
        for bags in all_the_bags[key]:
            for color in base_color_in_list:
                if color in bags and key not in base_color_in_list:
                    base_color_in_list.append(key)
                    new_color = True

    if new_color:
        base_color_in_list = get_substitute_colors(base_color_in_list)

    return base_color_in_list


subs = get_substitute_colors(["shiny gold"])
print(f"bag colors that can contain shiny gold: {len(subs)-1}")

