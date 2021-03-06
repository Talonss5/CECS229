class Matrix:
    
    def __init__(self, Rowsp=[]):  #FIXME: Replace with your code
        self.Rowsp=Rowsp
        self.Colsp=[]
        col=[]
        if len(self.Rowsp)==0 and len(self.Colsp)==0:
            self.Rowsp=[]
            self.Colsp=[]
        else:
            for i in range(len(self.Rowsp[0])):
                tempcol=[]
                for j in self.Rowsp:
                    tempcol.append(j[i])
                col.append(tempcol)
                self.Colsp=col
        pass
    
    def __add__(self, other):
        #FIXME: REPLACE WITH IMPLEMENTATION
        outputadd= Matrix([])
        add=[]
        if len(self.Rowsp)!=len(other.Rowsp):
            raise ValueError("Dimension mismatch")
        else:
            for subself, subother in zip(self.Rowsp,other.Rowsp):
                for selfitems, otheritems in zip(subself,subother):
                    add.append(selfitems+otheritems)
                for i in range(0,len(add),len(subself)):
                    templist=add[i:i+len(subself)]
                outputadd.Rowsp.append(templist)
            for i in range(len(outputadd.Rowsp[0])):
                tempcol=[]
                for j in outputadd.Rowsp:
                    tempcol.append(j[i])
                outputadd.Colsp.append(tempcol)
        return outputadd
        pass 
    
    def __sub__(self, other):
        #FIXME: REPLACE WITH IMPLEMENTATION
        outputsub= Matrix([])
        sub=[]
        if len(self.Rowsp)!=len(other.Rowsp):
            raise ValueError("Dimension mismatch")
        else:
            for subself, subother in zip(self.Rowsp,other.Rowsp):
                for selfitems, otheritems in zip(subself,subother):
                    sub.append(selfitems-otheritems)
                for i in range(0,len(sub),len(subself)):
                    templist=sub[i:i+len(subself)]
                outputsub.Rowsp.append(templist)

            for i in range(len(outputsub.Rowsp[0])):
                tempcol=[]
                for j in outputsub.Rowsp:
                    tempcol.append(j[i])
                outputsub.Colsp.append(tempcol)
        return outputsub
        pass
        
    def __mul__(self, other):
        outputmul=Matrix([])
        if type(other) == float:
            #print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  #REPLACE
            mul=[]
            for subself in self.Rowsp:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.Rowsp.append(templist)
            
        elif type(other) == Matrix:
            #print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") #REPLACE
            mul=[[0 for row in range(len(other.Rowsp[0]))]for column in range(len(self.Rowsp))]  
            if len(self.Rowsp[0])!=len(other.Rowsp):
                raise ValueError("Dimension mismatch")
            else:
                for i in range(len(self.Rowsp)):
                    for j in range(len(other.Rowsp[0])):
                        for k in range(len(other.Rowsp)):
                            mul[i][j]+=self.Rowsp[i][k]*other.Rowsp[k][j]
                outputmul.Rowsp=mul                  
        elif type(other) == Vec:
            #print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
            if len(self.Rowsp[0])!=len(other.elements):
                raise ValueError("Dimension mismatch")
            else:
                mul=[0 for column in range(len(self.Rowsp))]
                i=0
                x=0
                for j in range(len(self.Rowsp)):
                    i=0
                    row=0
                    for k in range(len(other.elements)):
                        row=row+self.Rowsp[j][i]*other.elements[i]
                        i+=1
                    mul[x]=row
                    x+=1    
                outputmul.Rowsp.append(mul)
        else:
            print("ERROR: Unsupported Type.")
        for i in range(len(outputmul.Rowsp[0])):
            tempcol=[]
            for j in outputmul.Rowsp:
                tempcol.append(j[i])
            outputmul.Colsp.append(tempcol)
        return outputmul
    
    def __rmul__(self, other):
        outputmul=Matrix([])
        if type(other) == float:
        #print("FIXME: Insert implementation of SCALAR-MATRIX multiplication")  #REPLACE
            mul=[]
            for subself in self.Rowsp:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.Rowsp.append(templist)
            for i in range(len(outputmul.Rowsp[0])):
                tempcol=[]
                for j in outputmul.Rowsp:
                    tempcol.append(j[i])
                outputmul.Colsp.append(tempcol)
            return outputmul
        else:
            print("ERROR: Unsupported Type.")
        

    def setCol(self,j,u):
        if len(u)!=len(self.Colsp[0]):
            raise ValueError("Incompatable column length")
        else:
            self.Colsp[j-1]=u
            for i in range(len(self.Rowsp)):
                self.Rowsp[i][j-1]=u[i]

    def setRow(self,i,v):
        if len(v)!=len(self.Rowsp[i-1]):
            raise ValueError("Incompatable row length")
        else:
            self.Rowsp[i-1]=v
            for j in range(len(self.Colsp)):
                self.Colsp[j][i-1]=v[j]
            

    def setEntry(self,i,j,a):
        self.Rowsp[i-1][j-1]=a
        self.Colsp[j-1][i-1]=a
        
    def getCol(self,j):
        return self.Colsp[j-1]
    
    def getRow(self, i):
        return self.Rowsp[i-1]

    def getEntry(self,i,j):
        return self.Rowsp[i-1][j-1]

    def getdiag(self, k):
        output=[]
        if k>=0:
            for i in range(len(self.Rowsp)-abs(k)):
                output.append(self.Rowsp[(i)%len(self.Rowsp)][(k+1 + i - 1)%len(self.Rowsp[0])])
        else:
            for i in range(abs(k),len(self.Rowsp)):
                output.append(self.Rowsp[(i)%len(self.Rowsp)][(k+1 + i - 1)%len(self.Rowsp[0])])
        return output
                
    
    def getColSpace(self):
        return self.Colsp

    def getRowSpace(self):
        return self.Rowsp
        
    def __str__(self):
        """prints the column """
        if len(self.Rowsp)==1:
            return "\n".join(" ".join(str(row))for row in self.Rowsp[0])
        else: 
            return "\n".join(" ".join(map(str,row))for row in self.Rowsp)


def png2graymatrix(filename):
    """
    takes a png file and returns a Matrix object of the pixels 
    INPUT: filename - the path and filename of the png file
    OUTPUT: a Matrix object with dimensions m x n, assuming the png file has width = n and height = m, 
    """
    #FIXME: a single line of code should go here
    image_data=image.file2image(filename)
    if not image.isgray(image_data):
        image_data = image.color2gray(image_data)#FIXME: make the image grayscale
    return Matrix(image_data) #FIXME


def graymatrix2png(img_matrix, path):
    """
    returns a png file created using the Matrix object, img_matrix
    INPUT: 
        * img_matrix - a Matrix object where img_matrix[i][j] is the intensity of the (i,j) pixel
        * path - the location and name under which to save the created png file 
    OUTPUT: 
        * a png file
    """
    return image.image2file(img_matrix.Rowsp,path)
    pass



