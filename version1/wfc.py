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
    if w >= W or h >= H:
        return False
    return np.array_equal(
        matrix1[:w,:h],
        matrix2[-w:,-h]
    )

def propagateWave(i,j):
    global checkedSlots
    checkedSlots = np.zeros(spaceMatrix.shape[:2])
    propagateWaveRecursive(i,j)

def propagateWaveRecursive(i,j):
    if checkedSlots[i,j]:
        return

def undeterminedSlots():
    l = []
    for i in range(spaceMatrix.shape[0]):
        for j in range(spaceMatrix.shape[1]):
            if np.count_nonzero(
                spaceMatrix[i,j,:]
            ) > 1:
                l.append((i,j))
    return l

def wfc(sample, w, h):
    global W
    global H
    global sampleMatrix
    W,H = w,h
    sampleMatrix = sample

    patterns = getPatterns()
    global spaceMatrix

    spaceMatrix = np.ones((sample.shape[0]-H, sample.shape[1]-W, len(patterns)))
    
    while True:
        undetermined = undeterminedSlots()
        if len(undetermined) == 0:
            break
        break