
var export_lar_obj = function(model){

	V,FV = model

	var s = "List of Vertices \n";

		for (var i = 0; i < V.length; i++){
		if (V[i][2]!= null)
			s += "v "+V[i][0]+"  "+V[i][1]+" "+V[i][2]+"\n"; 
		else
			s += "v "+V[i][0]+"  "+V[i][1]+"\n"; 	
		};
	s += "\n Face Definitions \n";
		for (var i = 0; i < FV.length; i++){
			if(FV[i][3] == null){
				s += "f "+FV[i][0]+" "+FV[i][1]+" "+FV[i][2]+"\n";	
			}else{
			s += "f " +FV[i][0]+" "+FV[i][1]+" "+FV[i][2]+" "+FV[i][3]+"\n";}
		};

	return(s);
}


