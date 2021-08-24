function inverter(lista) {
    let lista_invert = [];
    console.log(lista_invert, lista);
  
    for(let x = 0; x < lista.length; x++){
      lista_invert.unshift(lista[x]); 
    }
  
    console.log(lista_invert, lista)
    return lista_invert;
  }
inverter(["1", "2", "3"]);  