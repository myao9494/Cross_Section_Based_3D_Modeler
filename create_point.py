import numpy as np

def _angle_between(refvec):
    origin=[0,0]
    ang1 = np.arctan2(*origin[::-1])
    ang2 = np.arctan2(*refvec[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def create_point_random(x,num):
    """OpenVSP Xsec_point create
    
    Arguments:
        x {float} -- x_start point(Y=0)
        num {int} -- number of xsec_point
    
    Returns:
        list -- Xsec_point_list
    """
    start_and_end_point = [x,0]
    point = np.random.randn(num,2)
    point = np.insert(point,0,start_and_end_point,axis=0)
    pnt=point.tolist()
    pnt = sorted(pnt, key=_angle_between)
    pnt.append(start_and_end_point)
    return pnt