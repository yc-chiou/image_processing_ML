import math

def similarity(v1, v2):
    norm1 = normOfVector(v1)
    norm2 = normOfVector(v2)
    innerProduct = 0

    for i in range(0, len(v1)):
        innerProduct = innerProduct + v1[i] * v2[i]

    return innerProduct / (norm1 * norm2)

def normOfVector(v):
    norm = 0

    for i in range(0, len(v)):
        norm = norm + v[i] * v[i]

    return math.sqrt(norm)
    
if __name__ == "__main__":
    main()
