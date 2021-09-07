(function(){

    'use strict';
    document.addEventListener('DOMContentLoaded', function(){

        var btnAddProduct = document.getElementById('add-bolson');
        var productsContainer = document.getElementById('products-container')
        var childProductsContainer = document.getElementById('child')
        var btnRemoveProduct = document.getElementById('remove-bolson')

        btnAddProduct.addEventListener('click', addInput);
        btnRemoveProduct.addEventListener('click', removeInput)

        var num = 2

        function addInput(){

            var node = document.createElement('div')
            node.setAttribute('id', 'child')
            node.classList.add('mt-4')
            var label = document.createElement('label')
            label.setAttribute('id', 'disabledSelect')
            label.classList.add('form-label')
            textNode = document.createTextNode(`Producto #${num}`)
            label.appendChild(textNode)
            node.appendChild(label)
            var select = document.createElement('select')
            select.setAttribute('id', 'disabledSelect')
            select.classList.add('form-select', 'input')
            var option = document.createElement('option')
            var textNode = document.createTextNode('Seleccionar producto')
            option.appendChild(textNode)
            select.appendChild(option)
            node.appendChild(select)

            productsContainer.appendChild(node)
            num ++

        }

        function removeInput(){
            if (productsContainer.childElementCount > 1){
                productsContainer.lastChild.remove()
                num --
            }
            else{
                alert('El bolson debe contener al menos un producto')
            }   
        }

    });

})();