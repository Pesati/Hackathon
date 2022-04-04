function newInvestment(e) {
    e.preventDefault()
    console.log('Objetivo criado com sucesso')
    var li = document.createElement("li")
    var inputValue = document.getElementById("investment").value;
    var texto = document.createTextNode(inputValue);
    li.appendChild(texto)
  
    if (inputValue === '') {
      alert("Você precisa colocar um titulo!")
      console.warn("Tarefa sem titulo.")
  
    } else {
      document.getElementById("investments").appendChild(li)
      console.log(`Objetivo ${inputValue} criada com sucesso!`);
    }
    document.getElementById("investment").value = "";
    console.log("inputValue zerado.");
}

