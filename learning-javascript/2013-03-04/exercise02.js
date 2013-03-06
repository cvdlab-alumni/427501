for (var i = 1; i <= 10; i++) {
	var valore="";
	for (var j =1; j <= 10; j++){ 
		if(j!==10){ // se non è l'ultima colonna metti la ,
		valore+=i*j+","+"\t";}
		else 
			valore+=i*j+"\t";
	}
	console.log(valore);
}