window.onload=function(){

    //var btn = document.getElementById('btn-refresh')
    //btn.addEventListener('click', imprimir)

    var producto2 = document.getElementById('producto2')
    var producto3 = document.getElementById('producto3')
    var producto4 = document.getElementById('producto4')
    var producto5 = document.getElementById('producto5')

    producto2.style.display = 'none'
    producto3.style.display = 'none'
    producto4.style.display = 'none'
    producto5.style.display = 'none'

    var addProducto2 = document.getElementById('add-producto2')
    var addProducto3 = document.getElementById('add-producto3')
    var addProducto4 = document.getElementById('add-producto4')
    var addProducto5 = document.getElementById('add-producto5')

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

    function removeProducto2(){

        lista = [producto2, addProducto2]
        lista[0].style.display = 'none'
        lista[1].classList.remove('ocultar')
    }

    function removeProducto3(){

        lista = [producto3, addProducto3]
        lista[0].style.display = 'none'
        lista[1].classList.remove('ocultar')
    }

    function removeProducto4(){

        lista = [producto4, addProducto4]
        lista[0].style.display = 'none'
        lista[1].classList.remove('ocultar')
    }

    function removeProducto5(){

        lista = [producto5, addProducto5]
        lista[0].style.display = 'none'
        lista[1].classList.remove('ocultar')
    }

    // function agregarProducto(key){
    //     dic = {
    //         2: [producto2, addProducto2],
    //         3: [producto3, addProducto3],
    //         4: [producto4, addProducto4],
    //         5: [producto5, addProducto5]
    //     };
    //     dic[key][0].style.display = 'block'
    //     dic[key][1].classList.add('ocultar')
    // }


    function agregarProducto2(){

        lista = [producto2, addProducto2]
        lista[0].style.display = 'block'
        lista[1].classList.add('ocultar')
        

    }


    function agregarProducto3(){

        lista = [producto3, addProducto3]
        lista[0].style.display = 'block'
        lista[1].classList.add('ocultar')
    }

    function agregarProducto4(){

        lista = [producto4, addProducto4]
        lista[0].style.display = 'block'
        lista[1].classList.add('ocultar')
    }
    function agregarProducto5(){

        lista = [producto5, addProducto5]
        lista[0].style.display = 'block'
        lista[1].classList.add('ocultar')
    }






    function cargar(){
        fetch('http://127.0.0.1:8000/bolsones-venta').then(res=>res.json())
        .then(res=>{
            // console.log(res)
            // console.log(res.bolsonesventa)
            // console.log(res.bolsonesventa[0])
            // console.log(res.bolsonesventa[0].imagen)
            var bolsonesventa = res.bolsonesventa
            document.getElementById('divPrincipal').innerHTML="";
            
            
            for (var i in bolsonesventa){
                //console.log(bolsonesventa[i])
                
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
        //console.log('pvto')
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