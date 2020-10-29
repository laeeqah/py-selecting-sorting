#Task 1


items = [5, 3, 4, 1, 2]
def selectionSort( items ):
  
    for step in range(len(items)):
        min_value = step

        for location_of_smallest in range( step, len(items)):
            if items[location_of_smallest] < items[min_value] :
                min_value = location_of_smallest

        if min_value != step :
            temp = items[step]
            items[step] = items[min_value]
            items[min_value] = temp

    return items
bla = [5, 3, 4, 1, 2]
print(selectionSort(bla))


#Task 2

items = [5, 3, 4, 1, 2]

def num_search(items):
    item = [5, 3, 4, 1, 2]
    for i in item:
        return print (item.index(items))

    else:
        return "None"


num_search(4)


