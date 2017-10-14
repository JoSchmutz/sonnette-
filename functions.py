import math


def cercle(largeurImg, hauteurImg, rayonCercle, centreCercle, precision):
    return [(rayonCercle*(1+math.cos(2*math.pi/precision*x)),rayonCercle*(1+math.sin(2*math.pi/precision*x))) for x in xrange(0,precision+1)]
