import scipy.io as sio
import mat73
import numpy as np
import os
import sys

dlt1_mat = sio.loadmat(os.path.join(os.getcwd(), "dicStep3/" + 'DLTstruct_cam_201.mat'))
dlt2_mat = sio.loadmat(os.path.join(os.getcwd(), "dicStep3/" + 'DLTstruct_cam_202.mat'))
dltk = dlt1_mat['DLTstructCam']['DLTparams'][0][0] #the 11 dlt parameters for cam1 in matricx
dltl = dlt2_mat['DLTstructCam']['DLTparams'][0][0] #the 11 dlt parameters for cam2 in matricx, and turn it in a float array

dic2d = mat73.loadmat(os.path.join(os.getcwd(), "dicStep3/") +'DIC2DpairResults_C_201_C_202.mat')
dic2d_K = dic2d['DIC2DpairResults']['Points'][:5]
dic2d_L = dic2d['DIC2DpairResults']['Points'][5:]
k_corr = dic2d['DIC2DpairResults']['CorCoeffVec'][:5]
l_corr = dic2d['DIC2DpairResults']['CorCoeffVec'][5:]



corrComb = []
for i in range(len(k_corr)):
     tem = []
     for j in range(len(k_corr[i][0])):
          k = k_corr[i][0]
          l = l_corr[i][0]
          cor = max(k[j], l[j])
          tem.append(cor)
     corrComb.append(tem)

print(len(corrComb))
# for i in corrComb[0][:10]:
#      print(i)


# p = []
# for j in range(len(dic2d_K)): 
#      point = []
#      dic2d_k = dic2d_K[j][0]
#      dic2d_l = dic2d_L[j][0]
#      for i in range(len(dic2d_k)):
#           try:
#                u = np.array([ [dic2d_k[i][0] - dltk[3]],
#                               [dic2d_k[i][1] - dltk[7]],
#                               [dic2d_l[i][0] - dltl[3]],
#                               [dic2d_l[i][1] - dltl[7]] ])
#                a = np.array([ [ dltk[0] - dltk[8]*dic2d_k[i][0], dltk[1] - dltk[9]*dic2d_k[i][0], dltk[2] - dltk[10]*dic2d_k[i][0] ],
#                               [ dltk[4] - dltk[8]*dic2d_k[i][1], dltk[5] - dltk[9]*dic2d_k[i][1], dltk[6] - dltk[10]*dic2d_k[i][1] ],
#                               [ dltl[0] - dltl[8]*dic2d_l[i][0], dltl[1] - dltl[9]*dic2d_l[i][0], dltl[2] - dltl[10]*dic2d_l[i][0] ],
#                               [ dltl[4] - dltl[8]*dic2d_l[i][1], dltl[5] - dltl[9]*dic2d_l[i][1], dltl[6] - dltl[10]*dic2d_l[i][1] ], ])
#                u = np.reshape(u, (4,1))
#                a = np.reshape(a, (4,3))
#                tem = a.dot(a.T)
#                tem1 = np.dot(a.T, np.linalg.inv(tem))
#                p_3d = np.dot(tem1,u)
#                point.append(p_3d)
#           except:
#                u = np.array([ [dic2d_k[i][0] - dltk[3]],
#                               [dic2d_k[i][1] - dltk[7]],
#                               [dic2d_l[i][0] - dltl[3]],
#                               [dic2d_l[i][1] - dltl[7]] ])
#                a = np.array([ [ dltk[0] - dltk[8]*dic2d_k[i][0], dltk[1] - dltk[9]*dic2d_k[i][0], dltk[2] - dltk[10]*dic2d_k[i][0] ],
#                               [ dltk[4] - dltk[8]*dic2d_k[i][1], dltk[5] - dltk[9]*dic2d_k[i][1], dltk[6] - dltk[10]*dic2d_k[i][1] ],
#                               [ dltl[0] - dltl[8]*dic2d_l[i][0], dltl[1] - dltl[9]*dic2d_l[i][0], dltl[2] - dltl[10]*dic2d_l[i][0] ],
#                               [ dltl[4] - dltl[8]*dic2d_l[i][1], dltl[5] - dltl[9]*dic2d_l[i][1], dltl[6] - dltl[10]*dic2d_l[i][1] ], ])
#                print(type(dic2d_k[i][0]))
#                break
#                point.append(np.array([None,None,None]))
#      p.append(point)

# print(len(p))