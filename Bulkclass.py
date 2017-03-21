import math
class BulkCard (object):
    def __init__(self, kwrd):
        self.kwrd = kwrd

class Begin(BulkCard):
    """docstring for Begin"""
    def __init__(self, kwrd):
        BulkCard.__init__(self,kwrd)
    def wrtcrd(self):
        return "%s"%self.kwrd

class End(BulkCard):
    """docstring for End"""
    def __init__(self, kwrd):
        BulkCard.__init__(self,kwrd)
    def wrtcrd(self):
        return "\n%s"%self.kwrd

class creatGrid2D(BulkCard):
    """docstring for crearGrid2D"""
    def __init__(self, kwrd, nx, ny):
        BulkCard.__init__(self,kwrd)
        self.nx = nx
        self.ny = ny
    def wrtcrd(self):
        nodeset = []
        for i in range(1,self.nx+2):
            for j in range(1,self.ny+2):
              nodeset.append(self.kwrd+", %d , ,%d.0 , %d.0 , 0.0" %(j+(i-1)*(self.ny+1),i,j))
        nodes = ""
        for k in range(0, (self.nx + 1) * (self.ny + 1)):
            nodes = nodes +"\n" + nodeset[k]
        return nodes

class creatCQUAD4 (creatGrid2D):
    def __init__(self, kwrd, nx, ny):
        creatGrid2D.__init__(self, kwrd, nx, ny)
    def wrtcrd(self):
        elementset = []
        for i in range(1, self.nx * self.ny + 1):
            g1 = i + (math.ceil(float(i) / float(self.ny)) - 1)
            g2 = g1 + self.ny + 1
            g3 = g2 + 1
            g4 = g3 - (self.ny + 1)
            elementset.append(self.kwrd+", %d , 1 , %d ,%d ,%d  ,%d" % (i, g1, g2, g3, g4))
        elements = ""
        for j in range(0,self.nx*self.ny):
            elements = elements + "\n" + elementset[j]
        return elements

class creatGrid3D (creatGrid2D):
    def __init__(self,kwrd,nx,ny,nz):
        creatGrid2D.__init__(self,kwrd,nx,ny)
        self.nz = nz
    def wrtcrd(self):
        nodeset = []
        for k in range(1,self.nz+2):
            for i in range(1, self.nx + 2):
                for j in range(1, self.ny + 2):
                    nodeset.append(self.kwrd + ", %d , ,%d.0 , %d.0 , %d.0" % (j + (i - 1) * (self.ny + 1)+(k-1)*(self.nx+1)*(self.ny+1), i, j,k))
        nodes = ""
        for k in range(0, (self.nx + 1) * (self.ny + 1)*(self.nz + 1)):
            nodes = nodes +"\n" + nodeset[k]
        return nodes

class creatCHEXA (creatGrid3D):
    def __init__(self,kwrd,nx,ny,nz):
        creatGrid3D.__init__(self,kwrd,nx,ny,nz)
    def wrtcrd(self):
        elementset = []
        for i in range(1, self.nx * self.ny*self.nz + 1):
            k=i-self.nx * self.ny*(math.ceil(float(i)/float(self.nx * self.ny))-1)
            g1 =k+ (math.ceil(float(k) / float(self.ny)) - 1)+(self.nx + 1) * (self.ny + 1)*(math.ceil(float(i)/float(self.nx * self.ny))-1)
            g2 = g1 + self.ny + 1
            g3 = g2 + 1
            g4 = g3 - (self.ny + 1)
            g5 = g1 + (self.nx+1)*(self.ny+1)
            g6 = g2 + (self.nx + 1) * (self.ny + 1)
            g7 = g3 + (self.nx + 1) * (self.ny + 1)
            g8 = g4 + (self.nx + 1) * (self.ny + 1)
            elementset.append(self.kwrd + ", %d , 1 , %d ,%d ,%d  ,%d, %d,%d" % (i, g1, g2, g3, g4,g5,g6)+"\n,%d,%d"%(g7,g8))
        elements = ""
        for j in range(0, self.nx * self.ny*self.nz):
            elements = elements + "\n" + elementset[j]
        return elements

class Bulklist2D (object):
    def __init__(self,nx,ny):
        self.nx = nx
        self.ny = ny
    def write_bulklist(self):
        Bulklist = []
        Bulklist.append(Begin("BEGIN BULK").wrtcrd())
        Bulklist.append(creatCQUAD4("CQUAD4",self.nx,self.ny).wrtcrd())
        Bulklist.append(creatGrid2D("GRID",self.nx,self.ny).wrtcrd())
        Bulklist.append(End("ENDDATA").wrtcrd())
        return Bulklist

class Bulklist3D (Bulklist2D):
    def __init__(self,nx,ny,nz):
        Bulklist2D.__init__(self,nx,ny)
        self.nz = nz
    def write_bulklist(self):
        Bulklist = []
        Bulklist.append(Begin("BEGIN BULK").wrtcrd())
        Bulklist.append(creatCHEXA("CHEXA", self.nx, self.ny,self.nz).wrtcrd())
        Bulklist.append(creatGrid3D("GRID", self.nx, self.ny,self.nz).wrtcrd())
        Bulklist.append(End("ENDDATA").wrtcrd())
        return Bulklist
