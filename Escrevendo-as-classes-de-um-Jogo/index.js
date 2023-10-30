

  class heroi{
    constructor(nome, idade, tipo){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }
    
    atacar(){
        let ataque = ""

        if (this.tipo === "mago"){
           ataque = "magia"
        }else if(this.tipo ==="guerreiro"){
            ataque = "espada"
        }else if(this.tipo==="monge"){
            ataque = "artes marciais"
        }else if(this.tipo === "ninja"){
            ataque = "shuriken"
        }else{
            ataque = 'indefinido';
        }    
        console.log(`o ${this.tipo} atacou usando ${ataque}`)
    }
}    

let monge = new heroi("Naruto", 16, "monge")
let ninja = new heroi("Homem Aranha", 21, "ninja")

monge.atacar()
ninja.atacar()
