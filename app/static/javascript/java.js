const fileSelect = document.getElementById("fileSelect"),
    fileElem = document.getElementById("fileElem"),
    fileConteiner = document.getElementById("fileConteiner");
    
fileSelect.addEventListener("click", function (e) {
    if (fileElem) {
        fileElem.click();
    }
    e.preventDefault();
    }, false);
fileElem.addEventListener("change", handleFiles, false);
function handleFiles() {
    const fragmento= document.createDocumentFragment();
    const div = document.createElement("div");
    const img = document.createElement("img");
    img.src = URL.createObjectURL(this.files[0]);
    img.classList.add("imgFoto")
    img.onload = function() {
        URL.revokeObjectURL(this.src);
    }
    div.appendChild(img);
    fragmento.appendChild(div);
    fileConteiner.appendChild(fragmento)
}
const conteinerTalle= document.getElementById("conteinerTalle"),
btnTalle= document.getElementById("btnTalle");
let cantidadTalles=1;
btnTalle.addEventListener("click", e =>{
    e.preventDefault();
    let div= document.createElement("div");
    div.classList.add("inline");
    div.classList.add("conteinerInputTalle");
    let input= document.createElement("input");
    input.type="text"
    input.name="talles[]";
    input.classList.add("inputTalle");
    div.appendChild(input);
    conteinerTalle.appendChild(div);
    cantidadTalles++;
    console.log(cantidadTalles);
})

const tituloPrincipal= document.getElementById("tituloPrincipal");
const sticky =tituloPrincipal.offsetTop;
window.addEventListener("scroll",function(){
    if (window.scrollY >= sticky) {
        tituloPrincipal.classList.remove("tituloPrincipal")
        tituloPrincipal.classList.add("sticky")
    } else {
        tituloPrincipal.classList.add("tituloPrincipal")
        tituloPrincipal.classList.remove("sticky");
    }
})

const btnSubmitTalles= document.getElementById("btnSubmitTalles");
const tableTalles= document.getElementById("tableTalles");
btnSubmitTalles.addEventListener("click", e => {
    e.preventDefault();
    let conteiner= document.querySelector("#conteinerTalle");
    let match= conteiner.querySelectorAll("div > input");
    const talles=[];
    match.forEach(e=>{
        talles.push(e.value);
    })
    let table= document.createElement('table');
    let tr= document.createElement('tr');
    let th1= document.createElement('th');
    let th2= document.createElement('th');
    th1.innerHTML="Talle";
    th2.innerHTML="Cantidad";
    tr.appendChild(th1);
    tr.appendChild(th2);
    table.appendChild(tr);
    const fragmentoTalles= document.createDocumentFragment();
    for(var i=0; i<talles.length; i++){
        let tr= document.createElement('tr');
        let tdTalle= document.createElement('td');
        let tdInput= document.createElement('td');
        tdTalle.innerHTML=talles[i];
        tdInput.classList.add("conteinerTd")
        let input=document.createElement("input");
        input.type="text";
        input.classList.add("tdInput");
        input.classList.add("inputborde");
        input.classList.add("inputPrecio");
        input.name="stocks[]"
        tdInput.appendChild(input);
        tr.appendChild(tdTalle);
        tr.appendChild(tdInput);
        fragmentoTalles.appendChild(tr);
    }
    table.appendChild(fragmentoTalles);
    tableTalles.appendChild(table);
})