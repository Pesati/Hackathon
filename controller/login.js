var bodyparser = require('body-parser');
var fs = require('fs');
var data = fs.readFileSync('./API/perfis.json', 'utf8');
var accounts = JSON.parse(data)

function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    for (const id in accounts) {
        if (accounts[id].username == this.username && accounts[id].password == this.password) {
            alert("Logado com sucesso!");
            return false;
        } else {
            alert("Usuário ou senha incorreto")
            return false;
        }
    }
}