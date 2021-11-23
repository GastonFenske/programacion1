window.onload=function(){

    //var btn = document.getElementById('btn-refresh')
    //btn.addEventListener('click', imprimir)

    //agarra el producto numero dos, el div completo donde esta el select y el boton de trash
    var producto2 = document.getElementById('producto2')


    var producto3 = document.getElementById('producto3')
    var producto4 = document.getElementById('producto4')
    var producto5 = document.getElementById('producto5')

    var select2 = document.getElementById('select2')
    var select3 = document.getElementById('select3')
    var select4 = document.getElementById('select4')
    var select5 = document.getElementById('select5')


    //boton para sacarle el hidden al add producto 2
    var addProducto2 = document.getElementById('add-producto2')


    var addProducto3 = document.getElementById('add-producto3')
    var addProducto4 = document.getElementById('add-producto4')
    var addProducto5 = document.getElementById('add-producto5')

    //event listener del add producto2
    addProducto2.addEventListener('click', agregarProducto2)

    
    addProducto3.addEventListener('click', agregarProducto3)
    addProducto4.addEventListener('click', agregarProducto4)
    addProducto5.addEventListener('click', agregarProducto5)

    var trash2 = document.getElementById('trash-2')
    var trash3 = document.getElementById('trash-3')
    var trash4 = document.getElementById('trash-4')
    var trash5 = document.getElementById('trash-5')

    trash2.addEventListener('click', removeProducto2)
    trash3.addEventListener('click', removeProducto3)
    trash4.addEventListener('click', removeProducto4)
    trash5.addEventListener('click', removeProducto5)

    function agregarProducto2(){

        lista = [producto2, addProducto2]
        //lista[0].style.display = 'block'
        lista[0].classList.remove('hidden')
        lista[1].classList.add('hidden')
        

    }

    function removeProducto2(){

        lista = [producto2, addProducto2]
        lista[0].classList.add('hidden')
        lista[1].classList.remove('hidden')
        select2.value = 0
    }


    function agregarProducto3(){

        lista = [producto3, addProducto3]
        lista[0].classList.remove('hidden')
        lista[1].classList.add('hidden')
    }

    function removeProducto3(){

        lista = [producto3, addProducto3]
        lista[0].classList.add('hidden')
        lista[1].classList.remove('hidden')
        select3.value = 0
    }

    function agregarProducto4(){

        lista = [producto4, addProducto4]
        lista[0].classList.remove('hidden')
        lista[1].classList.add('hidden')
    }

    function removeProducto4(){

        lista = [producto4, addProducto4]
        lista[0].classList.add('hidden')
        lista[1].classList.remove('hidden')
        select4.value = 0
    }

    function agregarProducto5(){

        lista = [producto5, addProducto5]
        lista[0].classList.remove('hidden')
        lista[1].classList.add('hidden')
    }

    function removeProducto5(){

        lista = [producto5, addProducto5]
        lista[0].classList.add('hidden')
        lista[1].classList.remove('hidden')
        select5.value = 0
    }






    function cargar(){
        fetch('http://127.0.0.1:8000/bolsones-venta').then(res=>res.json())
        .then(res=>{

            var bolsonesventa = res.bolsonesventa
            document.getElementById('divPrincipal').innerHTML="";
            
            
            for (var i in bolsonesventa){

                
                var contenido='<div class="card mt-2" style="width: 18rem;">'
                contenido+=`<img src="${bolsonesventa[i].imagen}" class="card-img-top" alt="..."`
                contenido+=`<div class="card-body">
                                <h5 class="card-title">${bolsonesventa[i].nombre}</h5>
                            </div>`
                contenido+='</div>'
                document.getElementById('divPrincipal').innerHTML+=contenido
            }

    
    
        })
    }

    function imprimir(){
        cargar()
    }

    var btnPro = document.getElementById('btn-pro')
    btnPro.addEventListener('click', proveedores)
    function proveedores(page=1){
        var cookies = document.cookie
        var listaCookies = cookies.split(";")
        console.log(listaCookies)
        // fetch('http://127.0.0.1:8000/usuarios', {
        //     method: "GET",
        //     body: JSON.stringify({"page": page}),
        //     headers: {
        //         'Authorization': 123
        //     }
        // })
    }


}