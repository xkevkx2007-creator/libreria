const API_URL = "http://127.0.0.1:8000";


// ========================================
// LISTAR LIBROS
// ========================================

async function listarLibros() {

    const respuesta = await fetch(`${API_URL}/libros`);

    const libros = await respuesta.json();

    const lista = document.getElementById("lista-libros");

    lista.innerHTML = "";

    libros.forEach(libro => {

        lista.innerHTML += `
            <div class="libro">

                <h3>${libro[1]}</h3>

                <p>
                    <strong>Autor:</strong>
                    ${libro[2]}
                </p>

                <p>
                    <strong>Año:</strong>
                    ${libro[3]}
                </p>

                <p>
                    <strong>Género:</strong>
                    ${libro[4]}
                </p>

                <p>
                    <strong>Disponible:</strong>
                    ${libro[5] ? "Sí" : "No"}
                </p>

                <button onclick="editarLibro(${libro[0]})">
                    ✏️ Editar
                </button>

                <button onclick="eliminarLibro(${libro[0]})">
                    🗑️ Eliminar
                </button>

            </div>
        `;
    });
}


// ========================================
// AGREGAR LIBRO
// ========================================

async function agregarLibro() {

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const anio = document.getElementById("anio").value;
    const genero = document.getElementById("genero").value;


    if (!titulo || !autor || !anio || !genero) {

        alert("Todos los campos son obligatorios");

        return;
    }


    const libro = {

        titulo: titulo,
        autor: autor,
        anio: Number(anio),
        genero: genero,
        disponible: true

    };


    const respuesta = await fetch(`${API_URL}/libros`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(libro)

    });


    const resultado = await respuesta.json();

    console.log(resultado);


    // Limpiar formulario

    document.getElementById("titulo").value = "";
    document.getElementById("autor").value = "";
    document.getElementById("anio").value = "";
    document.getElementById("genero").value = "";


    listarLibros();
}


// ========================================
// ELIMINAR LIBRO
// ========================================

async function eliminarLibro(id) {

    const confirmar = confirm(
        "¿Seguro que quieres eliminar este libro?"
    );


    if (!confirmar) {

        return;

    }


    const respuesta = await fetch(
        `${API_URL}/libros/${id}`,
        {
            method: "DELETE"
        }
    );


    const resultado = await respuesta.json();

    console.log(resultado);


    listarLibros();
}


// ========================================
// EDITAR LIBRO
// ========================================

async function editarLibro(id) {

    const respuesta = await fetch(
        `${API_URL}/libros/${id}`
    );


    const libro = await respuesta.json();


    document.getElementById("editar-id").value = libro.id;

    document.getElementById("editar-titulo").value = libro.titulo;

    document.getElementById("editar-autor").value = libro.autor;

    document.getElementById("editar-anio").value = libro.anio;

    document.getElementById("editar-genero").value = libro.genero;


    document.getElementById(
        "formulario-editar"
    ).style.display = "block";
}


// ========================================
// GUARDAR EDICIÓN
// ========================================

async function guardarEdicion() {

    const id = document.getElementById("editar-id").value;

    const titulo = document.getElementById("editar-titulo").value;

    const autor = document.getElementById("editar-autor").value;

    const anio = document.getElementById("editar-anio").value;

    const genero = document.getElementById("editar-genero").value;


    if (!titulo || !autor || !anio || !genero) {

        alert("Todos los campos son obligatorios");

        return;
    }


    const libro = {

        titulo: titulo,

        autor: autor,

        anio: Number(anio),

        genero: genero,

        disponible: true

    };


    const respuesta = await fetch(
        `${API_URL}/libros/${id}`,
        {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(libro)

        }
    );


    const resultado = await respuesta.json();

    console.log(resultado);


    // Ocultar formulario

    document.getElementById(
        "formulario-editar"
    ).style.display = "none";


    listarLibros();
}


// ========================================
// CANCELAR EDICIÓN
// ========================================

function cancelarEdicion() {

    document.getElementById(
        "formulario-editar"
    ).style.display = "none";

}


// ========================================
// CARGAR LIBROS AL ABRIR
// ========================================

listarLibros();

async function buscarLibros() {

    const titulo = document.getElementById("busqueda").value;

    if (!titulo) {
        alert("Escribe algo para buscar");
        return;
    }

    const respuesta = await fetch(
        `${API_URL}/buscar?titulo=${encodeURIComponent(titulo)}`
    );

    const libros = await respuesta.json();

    const lista = document.getElementById("lista-libros");

    lista.innerHTML = "";

    libros.forEach(libro => {

        lista.innerHTML += `
            <div class="libro">

                <h3>${libro[1]}</h3>

                <p>
                    <strong>Autor:</strong>
                    ${libro[2]}
                </p>

                <p>
                    <strong>Año:</strong>
                    ${libro[3]}
                </p>

                <p>
                    <strong>Género:</strong>
                    ${libro[4]}
                </p>

                <p>
                    <strong>Disponible:</strong>
                    ${libro[5] ? "Sí" : "No"}
                </p>

                <button onclick="editarLibro(${libro[0]})">
                    ✏️ Editar
                </button>

                <button onclick="eliminarLibro(${libro[0]})">
                    🗑️ Eliminar
                </button>

            </div>
        `;
    });
}