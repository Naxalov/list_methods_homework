def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    label = 'apple'
    count = 0
    idx = 0
    idxs = []

    if fruits[idx]==label:
        count+=1
        idxs.append(idx)

    idx+=1

    if fruits[idx]==label:
        count+=1
        idxs.append(idx)
    idx+=1

    if fruits[idx]==label:
        count+=1
        idxs.append(idx)
    idx+=1

    if fruits[idx]==label:
        count+=1
        idxs.append(idx)
    idx+=1

    if fruits[idx]==label:
        count+=1
        idxs.append(idx)
    idx+=1
    
    return [count]+idxs 

fruits = ["apple", "banana", "apple", "pear", "apple"]

x=main(fruits)

print(x)