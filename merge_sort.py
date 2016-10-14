import pdb;

def callback(el1, el2):
    if el1 > el2:
        return 1
    elif el1 ==  el2:
        return 0
    else:
        return -1

def merge_sort(array, cb=callback):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left = array[0:midpoint]
    right = array[midpoint:]

    return merge(merge_sort(left), merge_sort(right), cb)


def merge(arr1, arr2, cb):
    result = []
    while len(arr1) > 0 and len(arr2) > 0:
        if cb(arr1[0], arr2[0]) == 1:
            result.append(arr2.pop(0))
        else:
            result.append(arr1.pop(0))

    result.extend(arr1)
    result.extend(arr2)
    return result

def main():
    myList = [112, 140, 62, 0, 23, 46]
    print merge_sort(myList)

    return None

if __name__ == "__main__":
    main()
