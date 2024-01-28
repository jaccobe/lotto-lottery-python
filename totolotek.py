import random


def roll():
    return [str(random.randrange(1, 44)) for x in range(7)]

def totolotek():
    rolls = []
    for x in range(1000):
        rolls += [roll()]
    return rolls


def into_dict(rolls_to_d):
    d: dict = {}
    for one_roll in rolls_to_d:
        for number in one_roll:
            if number in d.keys():
                d[number] += 1
            else:
                d.update({number: 1})
    return d


def count_percentage(dict_rolls):
    nums = dict_rolls
    l = []
    for x in list(nums.keys()):
        l.append([int(x), round((nums[x] / 7000) * 100, 2)])
    l = sorted(l, key=lambda x: x[0])
    return l


with (open('totolotek.txt', 'w') as f):
    rolls = totolotek()
    percentage = count_percentage(into_dict(rolls))
    for i in range(len(rolls)):
        f.write(f"Roll number {i + 1}: {rolls[i]}\n")
    f.write('\n')

    for x in range(len(percentage)):
        f.write(f"{percentage[x][0]}: {percentage[x][1]}%\n")
    f.write('\n')

    perc = sorted(percentage, key=lambda x: x[1],reverse=True)
    for x in range(len(perc)):
        f.write(f"{perc[x][0]}: {perc[x][1]}%\n")