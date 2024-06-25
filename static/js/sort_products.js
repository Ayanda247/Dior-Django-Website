document.addEventListener("DOMContentLoaded", function() {
    // Get the product container and products
    const productContainer = document.querySelector(".product-list");
    const products = Array.from(document.querySelectorAll(".product"));

    // Sorting functions
    const sortByPriceDesc = (a, b) => parseFloat(b.querySelector("p:nth-of-type(2)").textContent.substring(1)) - parseFloat(a.querySelector("p:nth-of-type(2)").textContent.substring(1));
    const sortByRatingDesc = (a, b) => parseFloat(b.querySelector("p:nth-of-type(3)").textContent.split(": ")[1]) - parseFloat(a.querySelector("p:nth-of-type(3)").textContent.split(": ")[1]);
    const sortByRandom = () => Math.random() - 0.5;

    // Function to apply sorting
    function applySort(sortFunction) {
        const sortedProducts = products.slice().sort(sortFunction);
        productContainer.innerHTML = "";
        sortedProducts.forEach(product => productContainer.appendChild(product));
    }

    // Event listeners for sorting options
    document.getElementById("sort-price").addEventListener("click", () => applySort(sortByPriceDesc));
    document.getElementById("sort-rating").addEventListener("click", () => applySort(sortByRatingDesc));
    document.getElementById("sort-trendy").addEventListener("click", () => applySort(sortByRandom));
});
