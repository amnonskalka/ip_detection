import itertools


def ip_options_old(a):
    tmp_list = []
    opt = {}
    ip_list = []
    opt_num = 0

    for x in a:
        if x.isdigit():
            if len(tmp_list) < 3:
                tmp_list.append(x)
            else:
                opt_dic = map(str, tmp_list)
                opt['opt' + str(opt_num)] = ''.join(opt_dic)
                tmp_list = []
                tmp_list.append(x)
                opt_num += 1
        elif x == '.':
            opt_dic = map(str, tmp_list)
            opt['opt' + str(opt_num)] = ''.join(opt_dic)
            ip_list.append(opt)
            tmp_list = []
            opt = {}

    opt_dic = map(str, tmp_list)
    opt['opt' + str(opt_num)] = ''.join(opt_dic)
    ip_list.append(opt)

    return ip_list


def store_details(opt, part_cnt, tmp_list):
    key = "part" + str(part_cnt)
    opt_dic = map(str, tmp_list)
    opt_dic = ''.join(opt_dic)
    opt.setdefault(key, [])
    opt[key].append(opt_dic)



def ip_finder(a):
    tmp_list = []
    opt = {}
    part_cnt = 0

    for x in a:
        if x.isdigit():
            if len(tmp_list) < 3:
                tmp_list.append(x)
            else:
                store_details(opt, part_cnt, tmp_list)
                tmp_list = []
                tmp_list.append(x)

        elif x == '.':
            store_details(opt, part_cnt, tmp_list)
            tmp_list = []
            part_cnt += 1

    store_details(opt, part_cnt, tmp_list)

    return opt


def ip_comb(x):
    allNames = sorted(x)
    combinations = list(itertools.product(*(x[Name] for Name in allNames)))
    for item in combinations:
        ip_com = ".".join(item)
        print(ip_com)
        try:
            f = open("ip_combination.txt", "a")
            f.write(ip_com + "\n")
            f.close()
        except Exception:
            print("Could not save file")