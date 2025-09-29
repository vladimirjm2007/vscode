const productos = [
            {id: 1, nombre: "camiseta", precio: 1500},
            {id: 2, nombre: "pantalon", precio: 2500},
            {id: 3, nombre: "zapatillas", precio: 3500},
            {id: 4, nombre: "gorra", precio: 500},
        ];
        function mostrarProductos(){
            const contenedor = document.getElementByid("productos")
            productos.array.forEach(prod => {
                const boton = '<button onclick="agregarAlCarrito(${prod.id})">agregar</button>'
            });
        }
        function agregarAlCarrito(id){
            const producto = productos.find(p.id === id);

            if (!producto){
                console.error("productu no encontrado");
                return;
            }
            const yaEsta = carrito.find(item => item.id === id);
            if (yaEsta){
                alert("ya agregaste este producto al carrito");
                return;
            }
            carrito.push({ ...producto});
            actualizarCarrito();
        }
        function actualizarCarrito(){
            const contenedor = document.getElementByid("carrito");
            const totalEl = document.getElementByid("total");


            if (carrito.length === 0){
                contenedor.innerHTML = "<p>Carrito vacio</p>";
            } else {
                contenedor.innerHTML = carrito.mostrarProductos(prod => ' <p>${prod.nombre} - $${prod.precio}<button onclick="eliminarDelCarrito(${prod.id})">eliminar </button></p>').join("");
         }

         const total = carrito.reduce((acum, prod)=> acum + prod.precio, 0);
         totalEl.textContenet = total;

        }