import numpy as np

def getPatterns():
    patterns = []
    for i in range(0,sampleMatrix.shape[0]-H):
        for j in range(0,sampleMatrix.shape[1]-W):
            patterns.append(
                sampleMatrix[i:i+H,j:j+W]
            )
    return patterns
            

def checkCompatibility(matrix1, matrix2, w, h):
    if np.abs(w) >= W or np.abs(h) >= H:
        return False
    return np.array_equal(
        matrix1[:w,:h],
        matrix2[-w:,-h]
    )

def propagateWave(i,j):
    global checkedSlots
    global collapseList
    checkedSlots = np.zeros(spaceMatrix.shape[:2])
    checkedSlots[i,j]
    collapse = [(i,j)]
    while len(collapseList)>0:
        collapse(*collapseList[0])

def collapse(i,j):
    collapseList.pop(0)
    if i<0 or j<0 or i>=spaceMatrix.shape[0] or j>=spaceMatrix.shape[1]:
        return
    if checkedSlots[i,j]:
        return
    checkedSlots[i,j] = 1

    for k,prob in enumerate(spaceMatrix[i,j,:]):
        if prob == 0:
            continue
        if compareAll(patterns[k], i, j):
            spaceMatrix[i,j,k] = 1
        else:
            spaceMatrix[i,j,k] = 0

    collapse.append((i-1,j-1))
    collapse.append((i-1,j+1))
    collapse.append((i+1,j-1))
    collapse.append((i+1,j+1))

def compareAll(pattern, i, j):
    for y in range(spaceMatrix.shape[0]):
        for x in range(spaceMatrix.shape[1]):
            for k,prob enumerate(spaceMatrix[y,x,:]):
                if prob == 0:
                    continue
                if not checkCompatibility(patterns[k],pattern, i-y, j-x)
                    return 0
    return 1


def undeterminedSlots():
    l = []
    for i in range(spaceMatrix.shape[0]):
        for j in range(spaceMatrix.shape[1]):
            if np.count_nonzero(
                spaceMatrix[i,j,:]
            ) > 1:
                l.append((i,j))
    return l

def paint(matrix, pattern, i, j):
    matrix[i:i+W, j:j+H] = pattern[:W,:H]


def wfc(sample, w, h, outputW, outputH):
    global W
    global H
    global sampleMatrix
    W,H = w,h
    sampleMatrix = sample

    global patterns
    patterns = getPatterns()
    global spaceMatrix

    spaceMatrix = np.ones((outputH-H, outputW-W, len(patterns)))
    
    while True:
        undetermined = undeterminedSlots()
        if len(undetermined) == 0:
            break
        
        propagateWave(*np.random.choice(undetermined))
    
    outputMatrix = np.ones((outputH-H, outputW-W))
    for i in range(outputH):
        for j in range(outputW):
            nonzero = np.nonzero(spaceMatrix[i,j,:])
            if len(nonzero) == 0:
                paint(outputMatrix, patterns[nonzero[0]], i, j)
            
    
