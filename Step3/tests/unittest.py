import unittest
import sys 
import os
sys.path.append(os.path.join(os.getcwd(), "dicStep3"))
sys.path.append(os.path.join(os.getcwd(), "dicStep3/tests"))
from Step3 import reconstruction_3D

class Test3DReconstruction(unittest.TestCase):

    result = reconstruction_3D('DLTstruct_cam_201.mat', 'DLTstruct_cam_202.mat', 'DIC2DpairResults_C_201_C_202.mat')
    image1 = result[0]
    #import the 3D points to points
    #point1 = points[0]

    # for i in range(len(image1)):
        #a = image[i][0] - point[i][0]
        #b = image[i][1] - point[i][1]
        #c = image[i][2] - point[i][2]
        #def test_accuracy(self):
            #self.assertAlmostEqual(a,0)
            #self.assertAlmostEqual(b,0)
            #self.assertAlmostEqual(b,0)