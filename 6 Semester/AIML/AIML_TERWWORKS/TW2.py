#TW 2

SuccList = {
    'S': [['A', 3], ['B', 6], ['C', 5]], 
    'A': [['E', 8], ['D', 9]], 
    'B': [['G', 14], ['F', 12]], 
    'C': [['H', 7]], 
    'H': [['J', 6], ['I', 5]], 
    'I': [['M', 2], ['L', 10], ['K', 1]]
}

def best_first_search(start, goal):
    open_list = [[start, 5]]
    closed_list = []
    i = 1

    while open_list:
        print(f"\n<<<<<<<<<---({i})-->>>>>>>>>\n")
        n = open_list.pop(0)
        closed_list.append(n)
        print(f"N= {n}")
        print(f"CLOSED= {closed_list}")

        if n[0] == goal:
            return closed_list, True

        children = [child for child in SuccList.get(n[0], []) if child not in open_list and child not in closed_list]
        print(f"CHILD= {children}")

        open_list.extend(children)
        print(f"Unsorted OPEN= {open_list}")
        open_list.sort(key=lambda x: x[1])
        print(f"Sorted OPEN= {open_list}")

        i += 1

    return closed_list, False

start = input("Enter Source node >> ").upper()
goal = input("Enter Goal node >> ").upper()
path, found = best_first_search(start, goal)

print("Best First Search Path >>>>>", path, "<<<<", found)