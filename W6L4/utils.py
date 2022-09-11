import matplotlib.pyplot as plt
import numpy as np
import cv2

def am_entropy(nimg , N=256):
    M = nimg.shape
    ssz = M[0] * M[1]
    hist,bins = np.histogram(nimg.flatten(),N,[0,N])
    hist = hist / ssz
    ent = -np.sum( hist * np.log2(hist+0.0001))
    return ent

# function to compute the image power. input could be graylevel or color. 
#
def am_power(a):
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

# function to compute the image energy. input could be graylevel or color. 
#
def am_energy(a):
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


# function to computer tha valid part of an image after convolution
# a is image, and N is the size of filter convolved previosly with a
#
def am_valid_part(a,N=3):
    cff = int(N/2)
    M = a.shape
    return a[cff:M[0]-cff, cff:M[1]-cff, :]


def idealHighPass(M, N, D0):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts:
    filter = np.ones((M, N), dtype=np.uint8)
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. If the pixel is within D0, it is changed to 0:
    for i in range(M):
        for j in range(N):
            if ( (i-M/2)**2 + (j-N/2)**2)**0.5 <= D0:
                filter[i,j]= 0
            
    return filter



#
# The function generates an ideal low pass filter for frequency domain, 
# M and N are size of the filter/image, D0 is the cut_off point. 
# 
def idealLowPass(M, N, D0):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts:
    filter = np.ones((M, N), dtype=np.uint8)
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. If the pixel is within D0, it is changed to 0:
    for i in range(M):
        for j in range(N):
            if ( (i-M/2)**2 + (j-N/2)**2)**0.5 >= D0:
                filter[i,j]= 0
            
    return filter



# 
# this function generates a lowpass Gaussian filter
# image and filter size is MxN , STD of the Gaussian is D0 which is also the cut_off
# point of the filter
# 
def GaussLowPass(M, N, D0):
    filter = np.zeros((M, N))
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    for i in range(M):
        for j in range(N):
            d = ( (i-M/2)**2 + (j-N/2)**2 )**0.5
            filter[i,j]= np.exp(-((d/2/D0)**2) )
            
    return filter


def ButterworthLowPass(M, N, D0, n_o):
    #  
    filter = np.zeros((M, N))
    # normalized cut_off frequency is mapped to real index
    D0 = D0 * min(M,N) / 2
    n_o = 2 * n_o
    for i in range(M):
        for j in range(N):
            d = ( (i-M/2)**2 + (j-N/2)**2 )**0.5
            filter[i,j]= 1 / ( 1 + (d/D0)**n_o )
            
    return filter