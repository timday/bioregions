import geojson
import math
import numpy as np

# cos & sin functions using degrees
def cd(a):
    return np.cos((math.pi/180.0)*a)

def sd(a):
    return np.sin((math.pi/180.0)*a)

# XYZ point on sphere surface
# longitude 0 is XZ plane
# Z is pole
def pd(longitude,latitude):
    return np.array([cd(latitude)*cd(longitude),cd(latitude)*sd(longitude),sd(latitude)])

def sub(p,q):
    return (p[0]-q[0],p[1]-q[1],p[2]-q[2])
    
def dot(p,q):
    return p[0]*q[0]+p[1]*q[1]+p[2]*q[2]

def lerp(q,k,p):
    j=1.0-k
    return (
        j*q[0]+k*p[0],
        j*q[1]+k*p[1],
        j*q[2]+k*p[2]
    )

def cross(p,q):
    return (
        p[1]*q[2]-p[2]*q[1],
        p[2]*q[0]-p[0]*q[2],
        p[0]*q[1]-p[1]*q[0]
    )

def normalized(v):
    m=math.sqrt(v[0]**2+v[1]**2+v[2]**2)
    return (v[0]/m,v[1]/m,v[2]/m)


def summarize():
    n=0
    for f in g.features:
        if n==0:
            # print(f.properties['LICENSE'])
            print('Polygon with rings:')
            for i in range(len(f.geometry.coordinates)):
                print(len(f.geometry.coordinates[i]))
        assert f.type=='Feature'
        print('{:4d}: {:20s} {:s}'.format(n,f.geometry.type,f.properties['BIOREGIO_1']))
        n+=1

class PolygonTester:
    
    def __init__(self,coords):
        assert coords[0]==coords[-1]  # Geojson spec requires end-points to be duplicated

        # Old way:
        #self._pts=np.array(list(map(lambda c: pd(*c),coords)))

        # This is a few seconds faster
        self._coords=np.array(coords)
        r=cd(self._coords[:,1])
        x=r*cd(self._coords[:,0])
        y=r*sd(self._coords[:,0])
        z=sd(self._coords[:,1])
        self._pts=np.stack([x,y,z],1)
        
        # Kinda-centroid, should be somewhere useful in/near/around polygon
        self._pc=normalized(np.mean(np.array(self._pts),axis=0))

        # Furthest polygon point from centroid
        # Old way:
        # self._furthest=min(map(lambda p: dot(p,self._pc),self._pts))
        # Faster:
        self._furthest=np.amin(self._pc[0]*self._pts[:,0] + self._pc[1]*self._pts[:,1] + self._pc[2]*self._pts[:,2])
        
    def contains(self,longitude,latitude):

        pt=pd(longitude,latitude)

        # We want to count polygon crossings on the great circle between pt and the assumed-outside -pc
        # Dot product between pt and pc defines the "distance" from pc +1 (near) to -1 (far)
        # This is threshold at which we're interested in crossings
        t=dot(pt,self._pc)
        
        # If we're testing a bit more than furthest from polygon centroid then early out.
        if t<self._furthest-0.05:
            return False

        # Defines a great circle plane through pt and pc
        n=normalized(cross(pt,self._pc))

        # Defines the side of the centroid we're interested in.  Points towards pt
        s=normalized(cross(self._pc,n))
        assert dot(s,pt)>0.0

        # Cut the polygon with the great circle plane
        pn=n[0]*self._pts[:,0] + n[1]*self._pts[:,1] + n[2]*self._pts[:,2]
        
        c=0
        for i in range(len(self._pts)-1):

            d0=pn[i]    # dot(p0,n)
            d1=pn[i+1]  # dot(p1,n)

            if (d0<=0.0 and d1>0.0) or (d0>=0.0 and d1<0.0):  # Test segment is cut by great circle plane

                p0=self._pts[i]
                p1=self._pts[i+1]
                
                # Compute intersection point.
                # p0 -|--- p1 : d0 small, d1 big: k small
                # p0 ---|- p1 : d0 big, d1 small: k big
                k= -d0/(d1-d0)  # This would just be d0/(-d1+d0) = -d0/(d1-d0) for decreasing case
                # NB And move it back to sphere surface.
                d=normalized(lerp(p0,k,p1))

                # Is the intersection between the test point and the "far" anti-centroid?
                if dot(d,s)>0.0 and dot(d,self._pc)<=t:
                    c+=1

        # Odd number of crossings means test point is in the polygon
        return c%2==1

class Bioregion:

    def __init__(self,feature,verbose=False):
        self._code=feature.properties['BIOREGION_']
        self._description=feature.properties['BIOREGIO_1']
        if verbose:
            print('{:4s}: {:15s} {}'.format(self._code,feature.geometry.type,self._description))
        if feature.geometry.type=='Polygon':
            self._polygons=[[PolygonTester(coords) for coords in feature.geometry.coordinates]]
        elif feature.geometry.type=='MultiPolygon':
            self._polygons=[]
            for polygon in feature.geometry.coordinates:
                self._polygons.append([PolygonTester(coords) for coords in polygon])
        else:
            raise RuntimeError('Unexpected geometry type: {}'.format(feature.geometry.type))

    def code(self):
        return self._code

    def description(self):
        return self._description

    def contains(self,longitude,latitude):
        for polys in self._polygons:
            if polys[0].contains(longitude,latitude) and not any(hole.contains(longitude,latitude) for hole in polys[1:]):
                return True
        return False

class Bioregions:

    def __init__(self,verbose=False):
        filename='Bioregions2020.geojson'
        print('Loading {}...'.format(filename))
        g=geojson.load(open(filename))
        print('  ',g.features[0].properties['LICENSE'])
        assert g.type=='FeatureCollection'
        self._bioregions=[Bioregion(f,verbose) for f in g.features]
        print('..loaded {} bioregions'.format(len(self._bioregions)))
        self._descriptionForCode={r.code():r.description() for r in self._bioregions}
        
    # Returns a list of bioregion code(s) covering the given point
    def at(self,longitude,latitude):
        return [region.code() for region in self._bioregions if region.contains(longitude,latitude)]

    def descriptionForCode(self,c):
        return self._descriptionForCode[c]
