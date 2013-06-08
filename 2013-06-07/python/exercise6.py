from pyplasm import *
import numpy


def export_lar_obj(model):

	V,FV = model

	s = "List of Vertices\n";

	for i in numpy.arange(0,len(V),1):
		if (V[i][2]!= None):
			s += "v "+str(V[i][0])+" "+str(V[i][1])+" "+str(V[i][2])+'\n'; 
		else:
			s += "v "+str(V[i][0])+" "+str(V[i][1])+'\n'; 
				
	s += '\n'+" Face Definitions" +'\n';

	for i in numpy.arange(0,len(FV),1):
		if(FV[i][3] == None):
				s += "f "+str(FV[i][0])+" "+str(FV[i][1])+" "+str(FV[i][2])+"\n";	
		else:
			s += "f " +str(FV[i][0])+" "+str(FV[i][1])+" "+str(FV[i][2])+" "+str(FV[i][3])+"\n"
		

	return s;





