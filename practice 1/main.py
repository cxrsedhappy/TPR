import pandas as pd


def pareto(data):
    _pareto = {}
    column_names = data.columns

    for predominant in data.values:
        for dominant in data.values:

            # self compare check
            if predominant.all() == dominant.all():
                continue

            flag = True
            for i in range(len(column_names)):
                if column_names[i] == 'Name':
                    continue

                # side of value
                side = 1 if column_names[i].split('(')[1].strip(')') == "+" else -1

                # print(side, predominant[0], dominant[0], predominant[i], dominant[i])
                if side * predominant[i] < side * dominant[i]:
                    flag = False
                    break
            
            # all row gives "TypeError: unhashable type: 'numpy.ndarray'"
            if flag is True and predominant[0] not in _pareto:
                _pareto[predominant[0]] = f'{dominant[0]}'
            elif flag is True and predominant[0] in _pareto:
                _pareto[predominant[0]] += f' | {dominant[0]}'

    print(_pareto)


def main():
    data = pd.read_excel('practice 1/data.xlsx')
    pareto(data)


if __name__ == '__main__':
    main()