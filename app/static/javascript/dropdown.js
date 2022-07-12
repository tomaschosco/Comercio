const list= document.getElementById("listDrop");
console.log(list);
const lista= document.getElementById("conteiner");
lista.addEventListener('click', (e)=> {
    if(e.target &&e.target.tagName=="I" && e.target.id=="emote"){
        console.log(e.path[3].childNodes[3].classList[0]);
        clase=e.path[3].childNodes[3].classList[0];
        if(clase=="listDropdown"){
            e.path[3].childNodes[3].classList.remove("listDropdown");
            e.path[3].childNodes[3].classList.add("prueba");
        }else{
            e.path[3].childNodes[3].classList.remove("prueba");
        e.path[3].childNodes[3].classList.add("listDropdown");
        }
    }
    
})