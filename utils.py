import numpy as np

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

def idealHighPass(M, N, D0):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts:
    mask = np.ones((M, N), dtype=np.uint8)
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. If the pixel is within D0, it is changed to 0:
    for i in range(M):
        for j in range(N):
            if ( (i-M/2)**2 + (j-N/2)**2)**0.5 <= D0:
                mask[i,j]= 0
            
    return mask

def idealLowPass(M, N, D0):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts:
    mask = np.ones((M, N), dtype=np.uint8)
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. If the pixel is within D0, it is changed to 0:
    for i in range(M):
        for j in range(N):
            if ( (i-M/2)**2 + (j-N/2)**2)**0.5 >= D0:
                mask[i,j]= 0
            
    return mask

def GaussLowPass(M, N, D0):
    mask = np.zeros((M, N))
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    for i in range(M):
        for j in range(N):
            d = ( (i-M/2)**2 + (j-N/2)**2 )**0.5
            mask[i,j]= np.exp(-((d/2/D0)**2) )
            
    return mask

def ButterworthLowPass(M, N, D0, n_o):
    #  
    mask = np.zeros((M, N))
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    n_o = 2 * n_o
    for i in range(M):
        for j in range(N):
            d = ( (i-M/2)**2 + (j-N/2)**2 )**0.5
            mask[i,j]= 1 / ( 1 + (d/D0)**n_o )
            
    return mask

def ButterworthBandPass(M, N, D0, D1, n_o):
    #  
    mask = ButterworthLowPass(M, N,D0,n_o)
    mask = ButterworthLowPass(M, N,D1,n_o) - mask
        
    mask = mask * (1/np.max(mask)) 
    return mask

int2bin = lambda x, n: format(x, 'b').zfill(n)
                   

def horder(b,nn): 
    jj = int2bin(b,nn)
    kk = ''
    for j in range(nn): 
        kk = kk+jj[nn-1-j] 
    
    kkk=np.zeros(nn) 
    kkk[0] = kk[0] 
    for j in range(1,nn):
        kkk[j] = int(kkk[j-1]) ^ int(kk[j]) 
        
    k=0
    for j in range(nn):
        k = k + int(kkk[j]) * 2**(nn-1-j)  

    return int(k)

def ordhad(n): 
    h = hadamard(n)
    hh = hadamard(n)
    nn = np.log2(n)
    for i in range(n):
        k = horder(int(i) , int(nn)) 
        hh[k][:] = h[i][:]

    return hh

