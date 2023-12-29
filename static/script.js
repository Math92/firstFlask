document.addEventListener('DOMContentLoaded', function() {
    fetch('/ciudades')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('nombreCiudad');
            data.forEach(ciudad => {
                const option = document.createElement('option');
                option.value = ciudad.nombre;
                option.textContent = ciudad.nombre;
                select.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));
});

function getCiudad() {
    const nombreCiudad = document.getElementById('nombreCiudad').value;

    if (!nombreCiudad) {
        document.getElementById('resultado').innerHTML = "Por favor, selecciona una ciudad.";
        return;
    }

    fetch(`/ciudades/${nombreCiudad}`)
        .then(response => response.json())
        .then(data => {
            const resultadoDiv = document.getElementById('resultado');
            if (data.error) {
                resultadoDiv.innerHTML = `Error: ${data.error}`;
            } else {
                resultadoDiv.innerHTML = `Nombre: ${data.nombre}, Población: ${data.poblacion}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('resultado').innerHTML = "Error al buscar la ciudad. Por favor, intenta de nuevo.";
        });
}
