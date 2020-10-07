import scipy.io as sio
import mat73
import numpy as np


dlt1_mat = sio.loadmat('DLTstruct_cam_201.mat')
dlt2_mat = sio.loadmat('DLTstruct_cam_202.mat')
dltk = dlt1_mat['DLTstructCam']['DLTparams'][0][0] 
dltl = dlt2_mat['DLTstructCam']['DLTparams'][0][0]

print(type(dltl[0]))

# -8.66916837650970
# 0.684996173515583
# 0.0239477690356036

# 1220.24351231999
# -2.48839838112236
# -4.23731750956848

# -7.82566475828260
# 2520.50347319127
# -0.00150908988008185

# -0.00255300407389477
# 1.97877492168224e-05


# -7.79537190282398
# -3.69509099390530
# 0.0684230195761073

# 1147.44734031676
# -0.143760093131631
# -4.86122010155363

# -7.89985067221658
# 2495.26864615584
# -1.70436134530376e-05
# -0.00297504657859031
# -4.80718245816379e-05

#p1(1217, 449)
#p2(1198.82602191775, 648.290666073440)
# 1.03606647071912	2.04935870216986	248.616069879110

# u = np.array([[1217 - 1.22024351e+03],[449 - 2.52050347e+03],[1198.82602191775 - 1.14744734e+03],[648.290666073440 - 2.49526865e+03]])

# a = np.array([[-8.66916838e+00 - (-1.50908988e-03*1217), 6.84996174e-01 - (-2.55300407e-03 * 1217), 2.39477690e-02 - (1.97877492e-05 * 1217)],
#               [-2.48839838e+00 - (-1.50908988e-03 * 449), -4.23731751e+00 - (-2.55300407e-03 * 449), -7.82566476e+00 - (1.97877492e-05 * 449)],
#               [-7.79537190e+00 - (-1.70436135e-05*1198.82602191775), -3.69509099e+00 - (-2.97504658e-03 * 1198.82602191775),  6.84230196e-02 - (-4.80718246e-05 * 1198.82602191775)],
#               [-1.43760093e-01 - (-1.70436135e-05 * 648.290666073440), -4.86122010e+00 - (-2.97504658e-03 * 648.290666073440), -7.89985067e+00 - (-4.80718246e-05 * 648.290666073440)]])

# tem = np.dot(a,a.T)
# tem1 = np.dot(a.T, np.linalg.inv(tem))
# p_3d = np.dot(tem1,u)
# print(u)

# -6.83260599604 3.79200212719 -0.000133921776400002
# -1.81081702388 -3.09101868257 -7.8345494593908
# -7.77493957262869 -0.128527733478593 0.126052773851546 
# -0.132710877451787 -2.93252517105229 -7.8686861548107

# -3.24351000000001 -2071.50347 51.3786819177501 -1846.97798392656

# 1.03606647071917	2.04935870216987	248.616069879110