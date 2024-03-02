import numpy as np


def ft_invert(array: np.array) -> np.array:
 return 255 - array
def ft_red(array2: np.array) -> np.array:
 array= array2.copy()
 array[:,:,1:] = array[:,:,1:]*0
 return array
#your code here
def ft_green(array2: np.array) -> np.array:
 array= array2.copy()
 array[:,:,0] = array[:,:,0]-array[:,:,0]
 array[:,:,2] = array[:,:,2]-array[:,:,2]
 return array
#your code here
def ft_blue(array2: np.array) -> np.array:
 array= array2.copy()
 array[:,:,0] = 0
 array[:,:,1] = 0
 return array
#your code here
def ft_grey(array2: np.array) -> np.array:
 array= array2.copy()
 array[:,:,0] = array2[:,:,1]
 array[:,:,2] = array2[:,:,1]
 return array
 