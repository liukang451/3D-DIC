# from Step2 import Step2
from Step3.Step3 import Step3

# def main():
#     '''
#     step1
#     '''
    
#     # Result_2 = Step2()

#     '''
#     step3 & 4
#     '''

# if __name__ == '__main__':
# 	main()

a = Step3('DLTstruct_cam_201.mat', 'DLTstruct_cam_202.mat', 'DIC2DpairResults_C_201_C_202.mat').result()
print(a.keys())