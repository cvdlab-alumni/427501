for (var i = 1; i <= 10; i++) {
	var valore="";
	for (var j =1; j <= 10; j++){ 
		if(j!==10){ //se non è ultima colonna metti la ,
			if(i==j)
			valore+=1+","+"\t";
		else
			valore+=0+","+"\t"
	}
	else{
	if(i==j)
			valore+=1+"\t";
		else
			valore+=0+"\t"
	}	}
	console.log(valore);
}