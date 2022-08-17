# CS4243 Utility Functions, by Prof Amir ###

def am_entropy(nimg , N=256):
    """
    function to compute the entropy of an image.
    :param nimg: nimg is the input image
    :param N: N is the number of graylevels, default is 256
    :return: nimg is supposed to be a graylevel image.
    """
    M = nimg.shape
    ssz = M[0] * M[1]
    hist,bins = np.histogram(nimg.flatten(),N,[0,N])
    hist = hist / ssz
    ent = -np.sum( hist * np.log2(hist+0.0001))
    return ent


def am_power(a):
    """
    function to compute the image power. input could be graylevel or color.
    """
    pa = 0.0
    dim1 = a.shape
    if len(dim1)==2:
        sz = dim1[0] * dim1[1]
        for i in range(dim1[0]):
            for j in range(dim1[1]):
                pa += a[i,j]**2
    elif len(dim1)==3:
        sz = dim1[0] * dim1[1] * dim1[2]
        for i in range(dim1[0]):
            for j in range(dim1[1]):
                for k in range(dim1[2]):
                    pa += a[i,j,k]**2
    pa = pa / sz
    return pa


def am_energy(a):
    """
    function to compute the image energy. input could be graylevel or color.
    """
    pa = 0.0
    dim1 = a.shape
    if len(dim1)==2:
        sz = dim1[0] * dim1[1]
        for i in range(dim1[0]):
            for j in range(dim1[1]):
                pa += a[i,j]**2
    elif len(dim1)==3:
        sz = dim1[0] * dim1[1] * dim1[2]
        for i in range(dim1[0]):
            for j in range(dim1[1]):
                for k in range(dim1[2]):
                    pa += a[i,j,k]**2
    return pa


def am_valid_part(a,N=3):
    """
    function to computer tha valid part of an image after convolution
    :param a: a is image
    :param N: N is the size of filter convolved previosly with a
    """
    cff = int(N/2)
    M = a.shape
    return a[cff:M[0]-cff, cff:M[1]-cff, :]
