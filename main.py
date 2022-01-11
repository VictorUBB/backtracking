def solution(x, DIM):
    """
    The candidate x is a solution if
    we have all the elements in the permutation
    """
    return len(x) == DIM


def solutionFound(x):
    print(x)


def consistent(x):
    # verify if there are no duplicates
    for i in range(len(x) - 1):
        if x[i] == x[-1]:
            return False
    return True


def validate(x, i):
    lng = len(x) - 1
    if lng == 0:
        return True
    elif lng == 1:
        if x[0] > x[1]:
            return False
        else:
            return True
    elif lng == DIM - 1:
        if i > x[lng - 1]:
            return False
        else:
            return True
    elif lng > 2:
        if x[lng - 2] > x[lng - 1]:
            if x[lng - 1] < i:
                return False
            else:
                return True

    return True


def backRec(x):
    x.append(the_list[0])  # add a new component to the candidate solution
    for i in the_list:
        x[-1] = i  # set current component
        if validate(x, i):
            if consistent(x):
                if solution(x, DIM):
                    solutionFound(x)
                backRec(x)  # recursive invocation to deal with next components

    x.pop()


def consistentIter(x):
    # verify if there are no duplicates
    for i in range(len(x) - 1):
        if x[i] == x[-1]:
            return False
    return True







def backIter(dim):
    index=0
    x = [the_list[0]]
    poz=[]
    while len(x) > 0:
        choosed = False
        while not choosed and index < dim:
            x[-1] = the_list[index]
            index += 1
            choosed = consistent(x)
        if choosed:
            if len(poz)<len(x):
                poz.append(index-1)
            else: poz[-1]=index-1
            if validate(x, x[-1]):
                if solution(x, DIM):
                    solutionFound(x)
                else:
                    x.append(0)
                    index=0
        else:
            x = x[:-1]
            poz=poz[:-1]
            if len(poz)>0:
                if poz[-1]+1<dim:
                    index = poz[-1]+1






DIM = 4
the_list = [16, 27, 18, 14]
#backIter(4)
backRec([])
