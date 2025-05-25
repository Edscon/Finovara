const loadingDiv = document.getElementById('loading');
const grid = document.getElementById('institutionsGrid');
const input = document.getElementById('searchInput');
let institutions = [];

// Función para pintar las cards
function renderInstitutions(filtered) {
    grid.innerHTML = '';

    filtered.forEach(inst => {
    const card = document.createElement('div');
    card.className = "flex flex-col items-center w-[120px] border border-gray-200 rounded cursor-pointer hover:shadow-md";

    card.innerHTML = `
        <img src="${inst.logo}" alt="${inst.name}" class="w-25 h-25 object-contain mb-2" />
        <span class="text-center text-sm font-medium px-3">${inst.name}</span>
    `;

    card.onclick = () => {
        alert("Has seleccionado: " + inst.name);
        // Aquí puedes añadir lógica para cerrar modal o seguir flujo
    };

    grid.appendChild(card);
    });
}

// Evento input para filtro
input.addEventListener('input', e => {
    const query = e.target.value.toLowerCase();
    const filtered = institutions.filter(inst =>
    inst.name.toLowerCase().includes(query)
    );
    renderInstitutions(filtered);
});

// Al cargar la página hacemos fetch al backend
window.addEventListener('DOMContentLoaded', () => {
  
    fetch('institutions/')
    .then(response => {
        if (!response.ok) throw new Error('Error en la petición');
        return response.json();
    })
    .then(data => {
        
        institutions = data;
        renderInstitutions(institutions);

        // Ocultar loader y mostrar buscador + grid
        loadingDiv.classList.add('hidden');
        input.classList.remove('hidden');
        grid.classList.remove('hidden');
    })
    .catch(error => {
        loadingDiv.innerHTML = '<span class="text-red-500">Error cargando instituciones.</span>';
        console.error(error);
      
    });
});