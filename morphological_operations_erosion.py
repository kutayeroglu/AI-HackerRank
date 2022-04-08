import numpy as np

## Sadly image hard coded by hand 
example_image = np.array([[0,0,0,0,0,0,0,0,0,0],
                          [0,1,1,1,1,1,1,1,0,0],
                          [0,0,0,0,1,1,1,1,0,0],
                          [0,0,0,0,1,1,1,1,0,0],
                          [0,0,0,1,1,1,1,1,0,0],
                          [0,0,0,0,1,1,1,1,0,0],
                          [0,0,0,1,1,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0]])

def erosion(img):
    count = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == 0:
                continue
            else:
                ## For this specific input we don't need to
                ## define edge cases 
                if img[i+1,j] == 0 or img[i-1,j] == 0 or img[i,j-1] == 0 or img[i, j+1] == 0 or img[i+1, j+1] == 0 or img[i+1, j-1] == 0 or img[i-1, j+1] == 0 or img[i-1, j-1] == 0:
                    continue
                else:
                    count += 1
                    continue
    print(count) ## As outputed, the answer is 6
    

erosion(example_image)
