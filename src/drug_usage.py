import sys

drug_pres = {} # store {drug name: (set of prescribers' ids)}
drug_cost = {} # store {drug name: cost sum}

def top_cost_drug():
    with open(get_file_path()[0], "r") as infile:

        for line in infile:
            # skip the header if has one
            if not line.split(",")[0].isdigit():
                continue

            # update dictionary `drug_pres` and `drug_cost`
            drug_pres, drug_cost = group_pres_cost(line)

    #output an file containing only column names if result is empty
    if ('drug_pres' not in locals()) and ('drug_cost' not in locals()):
        with open(get_file_path()[1], "w+") as file:
            file.write("drug_name,num_prescriber,total_cost")
            return

    # after group all input data, combine two dictionaries and sort results in descending
    res = combine_and_sort(drug_pres, drug_cost)

    # save result to file
    with open(get_file_path()[1], "w+") as file:
        file.write("drug_name,num_prescriber,total_cost")
        for line in res:
            strs=",".join(str(x) for x in line)
            file.write("\n" + strs)


def group_pres_cost(line):
    '''
    extract prescriber id, drug name, and drug cost from each line read in.
    for dictionary `drug_pres`: store drug name as key, unique prescribers' ids as value
    for dictionary `drug_cost`: store drug name as key, added drug cost as value
    '''

    # if certain record contains any missing value, skip this line
    try:
        id_pres = int(line.split(",")[0])
        name_drug = line.split(",")[3]
        cost_drug = float(line.split(",")[4].rstrip())
    except IndexError:
        return drug_pres, drug_cost

    if name_drug not in drug_pres:
        drug_pres[name_drug] = set([id_pres])
        drug_cost[name_drug] = cost_drug
    else:
        drug_pres[name_drug].add(id_pres)
        drug_cost[name_drug] += cost_drug

    return drug_pres, drug_cost


def combine_and_sort(drug_pres, drug_cost):
    '''
    extract drug name and number of unique prescribers from dictionary `drug_pres`,
    extract drug cost from dictionary `drug_cost`.
    then sort the list by the drug cost in descending order
    '''
    res = []
    for name in drug_pres.keys():
        res.append((name, len(drug_pres[name]), int(drug_cost[name])))

    res.sort(key = lambda x: x[2], reverse=True)
    return res


def get_file_path():
    '''
    get input and output path
    '''
    # make sure this file takes exactly 2 arguments
    if not len(sys.argv) == 3:
        print ("Invalid number of arguments. Run as: python3 drug_usage.py <input_file_path> <output_file_path>")
        sys.exit()

    file_in = sys.argv[1]
    file_out = sys.argv[2]
    return file_in, file_out


if __name__ == "__main__":
    top_cost_drug()
