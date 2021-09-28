window.onload=function(){

    //var btn = document.getElementById('btn-refresh')
    //btn.addEventListener('click', imprimir)



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