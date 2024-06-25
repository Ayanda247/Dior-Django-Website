document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.getElementById('searchIcon');
    const searchBar = document.getElementById('searchBar');
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    searchIcon.addEventListener('click', function (event) {
        event.preventDefault();
        searchBar.classList.toggle('hidden');
        searchInput.focus();
    });

    searchInput.addEventListener('input', function () {
        const query = searchInput.value;
        if (query.length > 2) {
            fetch(`/search/?query=${query}`)
                .then(response => response.json())
                .then(data => {
                    searchResults.innerHTML = '';
                    if (data.results.length > 0) {
                        data.results.forEach(product => {
                            const productElement = document.createElement('div');
                            productElement.classList.add('product-result');
                            productElement.innerHTML = `
                                <img src="${product.image}" alt="${product.name}">
                                <div>
                                    <h3>${product.name}</h3>
                                    <p>$${product.price}</p>
                                </div>
                            `;
                            searchResults.appendChild(productElement);
                        });
                    } else {
                        searchResults.innerHTML = '<p>No products found.</p>';
                    }
                });
        } else {
            searchResults.innerHTML = '';
        }
    });
});
