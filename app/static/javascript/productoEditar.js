const conteinerTalle= document.getElementById("conteinerTalle"),
btnAgregar= document.getElementById("btnTalle");
btnAgregar.addEventListener("click", (e)=>{
    e.preventDefault();
    let div= document.createElement("div");
    div.classList.add("inputsTalles");
    let inputNombre= document.createElement("input");
    inputNombre.type="text"
    inputNombre.name="tallesNombresNew[]";
    inputNombre.classList.add("inputTalle");

    let inputCantidad= document.createElement("input");
    inputCantidad.type="text"
    inputCantidad.name="tallesCantidadNew[]";
    inputCantidad.classList.add("inputTalle");
    
    let icono= document.createElement("i");
    icono.id="iconoX";
    icono.classList.add("fa-solid");
    icono.classList.add("fa-xmark");
    icono.classList.add("cruz");
    div.appendChild(inputNombre);
    div.appendChild(inputCantidad);
    div.appendChild(icono);
    conteinerTalle.appendChild(div);
})

conteinerTalle.addEventListener('click', (e)=> {
    if(e.target &&e.target.tagName=="I" && e.target.id=="iconoX"){
        console.log(e);
        console.log(e.path[1]);
        let respuesta= confirm("Estas seguro de eliminar el talle?");
        if(respuesta){
            e.path[1].children[0].defaultValue="";
            e.path[1].classList.add("none");
        }
    }
    
})
