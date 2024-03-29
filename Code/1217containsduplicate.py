def containsduplicate(array):
    hashset = set()
    for num in array:
        if num in hashset:
            return True
        hashset.add(num)
    return False

#hashmap/hashtable, sorting, array