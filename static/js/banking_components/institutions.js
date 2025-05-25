const loadingDiv = document.getElementById('loading');
const grid = document.getElementById('institutionsGrid');
const input = document.getElementById('searchInput');
let institutions = [];

// Función para pintar las cards
function renderInstitutions(filtered) {
    grid.innerHTML = '';

    const ul = document.createElement('ul');
    ul.className = "list-disc pl-5 grid gap-2 grid-cols-1 lg:grid-cols-2";

    filtered.forEach(inst => {
        const li = document.createElement('li');
        li.className = "flex items-center cursor-pointer py-2 hover:bg-gray-100 rounded";

        li.innerHTML = `
            <img src="${inst.logo}" alt="${inst.name}" class="w-8 h-8 object-contain mr-3" />
            <span class="text-sm font-medium">${inst.name}</span>
        `;

        li.onclick = () => {
            alert("Has seleccionado: " + inst.name);
        };

        ul.appendChild(li);
    });

    grid.appendChild(ul);
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