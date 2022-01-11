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



def backRec1(x):
    x.append(the_list[0])  # add a new component to the candidate solution

    while len(x) > 0:
        ok = 0
        while ok==0:
            x.append(0)
            for i in the_list:
                x[-1] = i  # set current component
                if validate(x, i):
                    if consistent(x):
                        if solution(x, DIM):
                            solutionFound(x)
                        ok=1
                        break

            x.pop()



def backIter(dim):
    index=0
    x = [the_list[0]]
    while len(x) > 0:
        choosed = False

        while not choosed and index < dim:
            x[-1] = the_list[index]
            index += 1
            choosed = consistent(x)
        if choosed:
            if solution(x, DIM):
                solutionFound(x)
            else:
                x.append(0)
                index=0
            # expand candidate solution
        else:
            x = x[:-1]
            # go back one component

def backIter1(dim):
     x =[-1] #candidate solution
     while len(x)>0:
         choosed = False
         while not choosed and x[-1]<dim-1:
             x[-1] = x[-1]+1 #increase the last component
             choosed = consistent(x)
         if choosed:
             if solution(x, dim):
                 solutionFound(x)
             x.append(-1) # expand candidate solution
         else:
            x = x[:-1] #go back one component


DIM = 4
the_list = [16, 27, 18, 14]
backRec1([])
