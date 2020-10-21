# Generated with SMOP  0.41
from libsmop import *
# triSurfaceDeformation.m

    
@function
def triSurfaceDeformation(F=None,Vref=None,Vdef=None,*args,**kwargs):
    varargin = triSurfaceDeformation.varargin
    nargin = triSurfaceDeformation.nargin

    ## function for computing deformation on triangular elements

    # INPUTS:
# * F: nFaces-by-3 array representing the list of vertices for triangular faces
# * Vref: nVertices-by-3 array representing the 3d positions of the vertices of F in the reference positions
# * Vdef: a cell array where each cell represents a deformed time frame
# and contains a nVertices-by-3 array representing the 3d positions of the
# vertices of F in the reference positions

    # OUTPUTS:
# * deformationStruct: a structure with the following fields:
#   - Fmat # deformation gradient tensor
#   - Cmat # deformation gradient tensor
#   - Lamda1 # deformation gradient tensor
#   - Lamda2 # deformation gradient tensor
#   - J # dilatation (volume change. in this case area change)
#   - Emat # Lagrangian strain tensor
#   - emat # Euler-Almansi strain tensor
#   - Emgn # Lagrangian strain magnitude
#   - emgn # Almansi strain magnitude
#   - d3 # Normal to the faces.
#   - Epc1 # smallest planar Lagrangian principal strain
#   - Epc2 # largest planar Lagrangian principal strain
#   - Epc1vec # 1st planar Lagrangian principal strain direction (corresponds to Epc1) in the reference conf.
#   - Epc1vecCur # 2nd planar Lagrangian principal strain direction (corresponds to Epc1) in the reference conf.
#   - Epc2vec # 1st planar Lagrangian principal strain direction (corresponds to Epc1) transformed into the deformed (current) conf. so it is planar in the current state
#   - Epc2vecCur # 2nd planar Lagrangian principal strain direction (corresponds to Epc1) transformed into the deformed (current) conf. so it is planar in the current state
#   - epc1 # smallest planar Almansi principal strain
#   - epc2 # largest planar Almansi principal strain
#   - epc1vec # 1st planar Almansi principal strain direction (corresponds to Epc1). it is planar in the current conf.
#   - epc2vec # 2nd planar Almansi principal strain direction (corresponds to epc2). it is planar in the current conf.

    # The deformation calculation is based on the Triangular Cosserat Point Theory (TCPE).
# Solav, Dana, et al. "Bone pose estimation in the presence of soft tissue artifact using triangular cosserat point elements." Annals of biomedical engineering 44.4 (2016): 1181-1190.
# Solav, Dana, M. B. Rubin, and Alon Wolf. "Soft tissue artifact compensation using triangular cosserat point elements (TCPEs)." International Journal of Engineering Science 85 (2014): 1-9.

    ##
    logicVcell=iscell(Vdef)
# triSurfaceDeformation.m:39
    if logical_not(logicVcell):
        error('the third input must be a cell array with one cell for each frame (time) containing a vertices 3D matrix).')

    deformationStruct=copy(struct)
# triSurfaceDeformation.m:44
    # number of frames
    nFrames=numel(Vdef)
# triSurfaceDeformation.m:47
    # number of triangular faces
    nFaces=size(F,1)
# triSurfaceDeformation.m:49
    # preallocate cells
    D1=cell(nFrames,1)
# triSurfaceDeformation.m:52
    D2=cell(nFrames,1)
# triSurfaceDeformation.m:53
    D3=cell(nFrames,1)
# triSurfaceDeformation.m:54
    d1=cell(nFrames,1)
# triSurfaceDeformation.m:55
    d2=cell(nFrames,1)
# triSurfaceDeformation.m:56
    d3=cell(nFrames,1)
# triSurfaceDeformation.m:57
    Drec1=cell(nFrames,1)
# triSurfaceDeformation.m:58
    Drec2=cell(nFrames,1)
# triSurfaceDeformation.m:59
    Dnorm=cell(nFrames,1)
# triSurfaceDeformation.m:60
    Fmat=cell(nFrames,1)
# triSurfaceDeformation.m:61
    Cmat=cell(nFrames,1)
# triSurfaceDeformation.m:62
    Lamda1=cell(nFrames,1)
# triSurfaceDeformation.m:63
    Lamda2=cell(nFrames,1)
# triSurfaceDeformation.m:64
    E=cell(nFrames,1)
# triSurfaceDeformation.m:65
    e=cell(nFrames,1)
# triSurfaceDeformation.m:66
    J=cell(nFrames,1)
# triSurfaceDeformation.m:67
    Emgn=cell(nFrames,1)
# triSurfaceDeformation.m:68
    emgn=cell(nFrames,1)
# triSurfaceDeformation.m:69
    Epc1=cell(nFrames,1)
# triSurfaceDeformation.m:70
    Epc1vec=cell(nFrames,1)
# triSurfaceDeformation.m:71
    Epc1vecCur=cell(nFrames,1)
# triSurfaceDeformation.m:72
    Epc2=cell(nFrames,1)
# triSurfaceDeformation.m:73
    Epc2vec=cell(nFrames,1)
# triSurfaceDeformation.m:74
    Epc2vecCur=cell(nFrames,1)
# triSurfaceDeformation.m:75
    epc1=cell(nFrames,1)
# triSurfaceDeformation.m:76
    epc1vec=cell(nFrames,1)
# triSurfaceDeformation.m:77
    epc2=cell(nFrames,1)
# triSurfaceDeformation.m:78
    epc2vec=cell(nFrames,1)
# triSurfaceDeformation.m:79
    EShearMax=cell(nFrames,1)
# triSurfaceDeformation.m:80
    eShearMax=cell(nFrames,1)
# triSurfaceDeformation.m:81
    EShearMaxVec1=cell(nFrames,1)
# triSurfaceDeformation.m:82
    EShearMaxVec2=cell(nFrames,1)
# triSurfaceDeformation.m:83
    EShearMaxVecCur1=cell(nFrames,1)
# triSurfaceDeformation.m:84
    EShearMaxVecCur2=cell(nFrames,1)
# triSurfaceDeformation.m:85
    eShearMaxVec1=cell(nFrames,1)
# triSurfaceDeformation.m:86
    eShearMaxVec2=cell(nFrames,1)
# triSurfaceDeformation.m:87
    Eeq=cell(nFrames,1)
# triSurfaceDeformation.m:88
    eeq=cell(nFrames,1)
# triSurfaceDeformation.m:89
    Area=cell(nFrames,1)
# triSurfaceDeformation.m:90
    hw=waitbar(0,'Calculating deformations and strains')
# triSurfaceDeformation.m:92
    for itime in arange(1,nFrames).reshape(-1):
        waitbar(itime / (nFrames))
        D1[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:98
        D2[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:99
        D3[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:100
        d1[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:101
        d2[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:102
        d3[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:103
        Drec1[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:104
        Drec2[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:105
        Dnorm[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:106
        Fmat[itime]=zeros(3,3,size(F,1))
# triSurfaceDeformation.m:107
        Cmat[itime]=zeros(3,3,size(F,1))
# triSurfaceDeformation.m:108
        Lamda1[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:109
        Lamda2[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:110
        E[itime]=zeros(3,3,size(F,1))
# triSurfaceDeformation.m:111
        e[itime]=zeros(3,3,size(F,1))
# triSurfaceDeformation.m:112
        J[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:113
        Emgn[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:114
        emgn[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:115
        Epc1[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:116
        Epc1vec[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:117
        Epc1vecCur[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:118
        Epc2[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:119
        Epc2vec[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:120
        Epc2vecCur[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:121
        epc1[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:122
        epc1vec[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:123
        epc2[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:124
        epc2vec[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:125
        EShearMax[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:126
        eShearMax[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:127
        EShearMaxVec1[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:128
        EShearMaxVec2[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:129
        EShearMaxVecCur1[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:130
        EShearMaxVecCur2[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:131
        eShearMaxVec1[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:132
        eShearMaxVec2[itime]=zeros(size(F,1),3)
# triSurfaceDeformation.m:133
        Eeq[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:134
        eeq[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:135
        Area[itime]=zeros(size(F,1),1)
# triSurfaceDeformation.m:136
        for itri in arange(1,nFaces).reshape(-1):
            # reference director vectors
            D1[itime][itri,arange()]=Vref(F(itri,2),arange()) - Vref(F(itri,1),arange())
# triSurfaceDeformation.m:141
            D2[itime][itri,arange()]=Vref(F(itri,3),arange()) - Vref(F(itri,1),arange())
# triSurfaceDeformation.m:142
            D3[itime][itri,arange()]=cross(D1[itime](itri,arange()),D2[itime](itri,arange())) / norm(cross(D1[itime](itri,arange()),D2[itime](itri,arange())))
# triSurfaceDeformation.m:143
            d1[itime][itri,arange()]=Vdef[itime](F(itri,2),arange()) - Vdef[itime](F(itri,1),arange())
# triSurfaceDeformation.m:146
            d2[itime][itri,arange()]=Vdef[itime](F(itri,3),arange()) - Vdef[itime](F(itri,1),arange())
# triSurfaceDeformation.m:147
            d3[itime][itri,arange()]=cross(d1[itime](itri,arange()),d2[itime](itri,arange())) / norm(cross(d1[itime](itri,arange()),d2[itime](itri,arange())))
# triSurfaceDeformation.m:148
            Dnorm[itime][itri]=dot(cross(D1[itime](itri,arange()),D2[itime](itri,arange())),D3[itime](itri,arange()).T)
# triSurfaceDeformation.m:151
            Drec1[itime][itri,arange()]=cross(D2[itime](itri,arange()),D3[itime](itri,arange())) / Dnorm[itime](itri)
# triSurfaceDeformation.m:152
            Drec2[itime][itri,arange()]=cross(D3[itime](itri,arange()),D1[itime](itri,arange())) / Dnorm[itime](itri)
# triSurfaceDeformation.m:153
            Area[itime][itri]=dot(0.5,Dnorm[itime](itri))
# triSurfaceDeformation.m:156
            for ii in arange(1,3).reshape(-1):
                for jj in arange(1,3).reshape(-1):
                    Fmat[itime][ii,jj,itri]=dot(d1[itime](itri,ii),Drec1[itime](itri,jj)) + dot(d2[itime](itri,ii),Drec2[itime](itri,jj)) + dot(d3[itime](itri,ii),D3[itime](itri,jj))
# triSurfaceDeformation.m:161
            if sum(sum(isnan(Fmat[itime](arange(),arange(),itri)))) == 0:
                # Cauchy-Green deformation tensor
                Cmat[itime][arange(),arange(),itri]=dot(Fmat[itime](arange(),arange(),itri).T,Fmat[itime](arange(),arange(),itri))
# triSurfaceDeformation.m:168
                __,eigValC=eig(Cmat[itime](arange(),arange(),itri),nargout=2)
# triSurfaceDeformation.m:169
                Lamdas=sqrt(concat([eigValC(1,1),eigValC(2,2),eigValC(3,3)]))
# triSurfaceDeformation.m:171
                __,ind1=min(abs(Lamdas - 1),nargout=2)
# triSurfaceDeformation.m:172
                Lamdas[ind1]=[]
# triSurfaceDeformation.m:173
                Lamda1[itime][itri]=Lamdas(1)
# triSurfaceDeformation.m:174
                Lamda2[itime][itri]=Lamdas(2)
# triSurfaceDeformation.m:175
                J[itime][itri]=det(Fmat[itime](arange(),arange(),itri))
# triSurfaceDeformation.m:178
                E[itime][arange(),arange(),itri]=dot(0.5,(dot(Fmat[itime](arange(),arange(),itri).T,Fmat[itime](arange(),arange(),itri)) - eye(3)))
# triSurfaceDeformation.m:181
                e[itime][arange(),arange(),itri]=dot(0.5,(eye(3) - inv(dot(Fmat[itime](arange(),arange(),itri),Fmat[itime](arange(),arange(),itri).T))))
# triSurfaceDeformation.m:184
                Emgn[itime][itri]=norm(E[itime](arange(),arange(),itri),'fro')
# triSurfaceDeformation.m:187
                emgn[itime][itri]=norm(e[itime](arange(),arange(),itri),'fro')
# triSurfaceDeformation.m:190
                eigVecE,eigValE=eig(E[itime](arange(),arange(),itri),nargout=2)
# triSurfaceDeformation.m:193
                __,D3Ind=max(abs(dot(eigVecE.T,D3[itime](itri,arange()).T)),nargout=2)
# triSurfaceDeformation.m:196
                eigVecPlanInd=concat([1,2,3])
# triSurfaceDeformation.m:197
                eigVecPlanInd[eigVecPlanInd == D3Ind]=[]
# triSurfaceDeformation.m:198
                Epc1[itime](itri),Epc1Ind=min(concat([eigValE(eigVecPlanInd(1),eigVecPlanInd(1)),eigValE(eigVecPlanInd(2),eigVecPlanInd(2))]),nargout=2)
# triSurfaceDeformation.m:199
                Epc2[itime](itri),Epc2Ind=max(concat([eigValE(eigVecPlanInd(1),eigVecPlanInd(1)),eigValE(eigVecPlanInd(2),eigVecPlanInd(2))]),nargout=2)
# triSurfaceDeformation.m:200
                Epc1vec[itime][itri,arange()]=eigVecE(arange(),eigVecPlanInd(Epc1Ind))
# triSurfaceDeformation.m:201
                Epc1vecCur[itime][itri,arange()]=dot(Fmat[itime](arange(),arange(),itri),Epc1vec[itime](itri,arange()).T)
# triSurfaceDeformation.m:202
                Epc1vecCur[itime][itri,arange()]=Epc1vecCur[itime](itri,arange()) / norm(Epc1vecCur[itime](itri,arange()))
# triSurfaceDeformation.m:203
                Epc2vec[itime][itri,arange()]=eigVecE(arange(),eigVecPlanInd(Epc2Ind))
# triSurfaceDeformation.m:204
                Epc2vecCur[itime][itri,arange()]=dot(Fmat[itime](arange(),arange(),itri),Epc2vec[itime](itri,arange()).T)
# triSurfaceDeformation.m:205
                Epc2vecCur[itime][itri,arange()]=Epc2vecCur[itime](itri,arange()) / norm(Epc2vecCur[itime](itri,arange()))
# triSurfaceDeformation.m:206
                eigVece,eigVale=eig(e[itime](arange(),arange(),itri),nargout=2)
# triSurfaceDeformation.m:209
                __,d3Ind=max(abs(dot(eigVece.T,d3[itime](itri,arange()).T)),nargout=2)
# triSurfaceDeformation.m:211
                eigVecPlanInd=concat([1,2,3])
# triSurfaceDeformation.m:212
                eigVecPlanInd[eigVecPlanInd == d3Ind]=[]
# triSurfaceDeformation.m:213
                epc1[itime](itri),epc1Ind=min(concat([eigVale(eigVecPlanInd(1),eigVecPlanInd(1)),eigVale(eigVecPlanInd(2),eigVecPlanInd(2))]),nargout=2)
# triSurfaceDeformation.m:214
                epc2[itime](itri),epc2Ind=max(concat([eigVale(eigVecPlanInd(1),eigVecPlanInd(1)),eigVale(eigVecPlanInd(2),eigVecPlanInd(2))]),nargout=2)
# triSurfaceDeformation.m:215
                epc1vec[itime][itri,arange()]=eigVece(arange(),eigVecPlanInd(epc1Ind))
# triSurfaceDeformation.m:216
                epc2vec[itime][itri,arange()]=eigVece(arange(),eigVecPlanInd(epc2Ind))
# triSurfaceDeformation.m:217
                # Max shear strain and its direction
            # Lagrangian
                EShearMax[itime][itri]=dot(0.5,(Epc2[itime](itri) - Epc1[itime](itri)))
# triSurfaceDeformation.m:221
                EShearMaxVec1[itime][itri,arange()]=dot((1 / sqrt(2)),(Epc1vec[itime](itri,arange()) + Epc2vec[itime](itri,arange())))
# triSurfaceDeformation.m:222
                EShearMaxVec2[itime][itri,arange()]=dot((1 / sqrt(2)),(Epc2vec[itime](itri,arange()) - Epc1vec[itime](itri,arange())))
# triSurfaceDeformation.m:223
                EShearMaxVecCur1[itime][itri,arange()]=dot((1 / sqrt(2)),(Epc1vecCur[itime](itri,arange()) + Epc2vecCur[itime](itri,arange())))
# triSurfaceDeformation.m:224
                EShearMaxVecCur2[itime][itri,arange()]=dot((1 / sqrt(2)),(Epc2vecCur[itime](itri,arange()) - Epc1vecCur[itime](itri,arange())))
# triSurfaceDeformation.m:225
                eShearMax[itime][itri]=dot(0.5,(epc2[itime](itri) - epc1[itime](itri)))
# triSurfaceDeformation.m:227
                eShearMaxVec1[itime][itri,arange()]=dot((1 / sqrt(2)),(epc1vec[itime](itri,arange()) + epc2vec[itime](itri,arange())))
# triSurfaceDeformation.m:228
                eShearMaxVec2[itime][itri,arange()]=dot((1 / sqrt(2)),(epc2vec[itime](itri,arange()) - epc1vec[itime](itri,arange())))
# triSurfaceDeformation.m:229
                Edev=E[itime](arange(),arange(),itri) - dot(dot((1 / 3),trace(E[itime](arange(),arange(),itri))),eye(3))
# triSurfaceDeformation.m:232
                Eeq[itime][itri]=sqrt(dot((2 / 3),sum(sum(multiply(Edev,Edev)))))
# triSurfaceDeformation.m:233
                edev=e[itime](arange(),arange(),itri) - dot(dot((1 / 3),trace(e[itime](arange(),arange(),itri))),eye(3))
# triSurfaceDeformation.m:234
                eeq[itime][itri]=sqrt(dot((2 / 3),sum(sum(multiply(edev,edev)))))
# triSurfaceDeformation.m:235
            else:
                Cmat[itime][arange(),arange(),itri]=concat([[NaN,NaN,NaN],[NaN,NaN,NaN],[NaN,NaN,NaN]])
# triSurfaceDeformation.m:238
                Lamda1[itime][itri]=NaN
# triSurfaceDeformation.m:239
                Lamda2[itime][itri]=NaN
# triSurfaceDeformation.m:240
                E[itime][arange(),arange(),itri]=concat([[NaN,NaN,NaN],[NaN,NaN,NaN],[NaN,NaN,NaN]])
# triSurfaceDeformation.m:241
                e[itime][arange(),arange(),itri]=concat([[NaN,NaN,NaN],[NaN,NaN,NaN],[NaN,NaN,NaN]])
# triSurfaceDeformation.m:242
                Emgn[itime][itri]=NaN
# triSurfaceDeformation.m:243
                emgn[itime][itri]=NaN
# triSurfaceDeformation.m:244
                J[itime][itri]=NaN
# triSurfaceDeformation.m:245
                Epc1[itime][itri]=NaN
# triSurfaceDeformation.m:246
                Epc1vec[itime][itri,arange()]=concat([NaN,NaN,NaN])
# triSurfaceDeformation.m:247
                Epc1vecCur[itime][itri,arange()]=concat([NaN,NaN,NaN])
# triSurfaceDeformation.m:248
                Epc2[itime][itri]=NaN
# triSurfaceDeformation.m:249
                Epc2vec[itime][itri,arange()]=concat([NaN,NaN,NaN])
# triSurfaceDeformation.m:250
                Epc2vecCur[itime][itri,arange()]=concat([NaN,NaN,NaN])
# triSurfaceDeformation.m:251
                epc1[itime][itri]=NaN
# triSurfaceDeformation.m:252
                epc1vec[itime][itri,arange()]=concat([NaN,NaN,NaN])
# triSurfaceDeformation.m:253
                epc2[itime][itri]=NaN
# triSurfaceDeformation.m:254
                epc2vec[itime][itri,arange()]=concat([NaN,NaN,NaN])
# triSurfaceDeformation.m:255
                EShearMax[itime][itri]=NaN
# triSurfaceDeformation.m:256
                eShearMax[itime][itri]=NaN
# triSurfaceDeformation.m:257
                Eeq[itime][itri]=NaN
# triSurfaceDeformation.m:258
                eeq[itime][itri]=NaN
# triSurfaceDeformation.m:259
                Area[itime][itri]=NaN
# triSurfaceDeformation.m:260

    delete(hw)
    # save all results in the structure

    deformationStruct.Fmat = copy(Fmat)
# triSurfaceDeformation.m:271

    deformationStruct.Cmat = copy(Cmat)
# triSurfaceDeformation.m:272

    deformationStruct.Lamda1 = copy(Lamda1)
# triSurfaceDeformation.m:273

    deformationStruct.Lamda2 = copy(Lamda2)
# triSurfaceDeformation.m:274

    deformationStruct.J = copy(J)
# triSurfaceDeformation.m:275

    deformationStruct.Emat = copy(E)
# triSurfaceDeformation.m:276

    deformationStruct.emat = copy(e)
# triSurfaceDeformation.m:277

    deformationStruct.Emgn = copy(Emgn)
# triSurfaceDeformation.m:278

    deformationStruct.emgn = copy(emgn)
# triSurfaceDeformation.m:279

    deformationStruct.d3 = copy(d3)
# triSurfaceDeformation.m:280

    deformationStruct.Epc1 = copy(Epc1)
# triSurfaceDeformation.m:281

    deformationStruct.Epc2 = copy(Epc2)
# triSurfaceDeformation.m:282

    deformationStruct.Epc1vec = copy(Epc1vec)
# triSurfaceDeformation.m:283

    deformationStruct.Epc1vecCur = copy(Epc1vecCur)
# triSurfaceDeformation.m:284

    deformationStruct.Epc2vec = copy(Epc2vec)
# triSurfaceDeformation.m:285

    deformationStruct.Epc2vecCur = copy(Epc2vecCur)
# triSurfaceDeformation.m:286

    deformationStruct.epc1 = copy(epc1)
# triSurfaceDeformation.m:287

    deformationStruct.epc2 = copy(epc2)
# triSurfaceDeformation.m:288

    deformationStruct.epc1vec = copy(epc1vec)
# triSurfaceDeformation.m:289

    deformationStruct.epc2vec = copy(epc2vec)
# triSurfaceDeformation.m:290

    deformationStruct.EShearMax = copy(EShearMax)
# triSurfaceDeformation.m:291

    deformationStruct.eShearMax = copy(eShearMax)
# triSurfaceDeformation.m:292

    deformationStruct.EShearMaxVec1 = copy(EShearMaxVec1)
# triSurfaceDeformation.m:293
    deformationStruct.EShearMaxVec2 = copy(EShearMaxVec2)
# triSurfaceDeformation.m:294
    deformationStruct.EShearMaxVecCur1 = copy(EShearMaxVecCur1)
# triSurfaceDeformation.m:295
    deformationStruct.EShearMaxVecCur2 = copy(EShearMaxVecCur2)
# triSurfaceDeformation.m:296
    deformationStruct.eShearMaxVec2 = copy(eShearMaxVec2)
# triSurfaceDeformation.m:297
    deformationStruct.Eeq = copy(Eeq)
# triSurfaceDeformation.m:298

    deformationStruct.eeq = copy(eeq)
# triSurfaceDeformation.m:299

    deformationStruct.Area = copy(Area)
# triSurfaceDeformation.m:300
    return deformationStruct

if __name__ == '__main__':
    pass
