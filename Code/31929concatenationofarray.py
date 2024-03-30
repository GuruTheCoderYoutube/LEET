def concatenationOfArray(array):
    res = [0] * (len(array)*2)
    for i in range(len(array)):
        res[i] = res[i+len(array)] = array[i]
    return res
# Array, Simulation, Array manipulation