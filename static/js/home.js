document.addEventListener("DOMContentLoaded", function() {
    setupCarousel();
    setupRandomProductsUpdate();
});

function setupCarousel() {
    const buttons = document.querySelectorAll("[data-carousel-button]");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const offset = button.dataset.carouselButton === "next" ? 1 : -1;
            const slides = button.closest("[data-carousel]").querySelectorAll("[data-slide-item] .slide-item");
            const activeSlide = button.closest("[data-carousel]").querySelector("[data-slide-item] .slide-item[data-active]");
            let newIndex = [...slides].indexOf(activeSlide) + offset;
            if (newIndex < 0) newIndex = slides.length - 1;
            if (newIndex >= slides.length) newIndex = 0;
            slides.forEach(slide => {
                slide.removeAttribute("data-active");
            });
            slides[newIndex].setAttribute("data-active", true);
        });
    });
}

// Function to fetch and update random products
function setupRandomProductsUpdate() {
    function updateRandomProducts() {
        $.ajax({
            url: "{% url 'update_random_products' %}",  // Replace with your Django URL
            type: "GET",
            success: function(data) {
                $(".product-content").html(data);  // Replace the content of .product-content
            },
            error: function(xhr, status, error) {
                console.error("Error fetching random products:", error);
            }
        });
    }

    // Update products initially
    $(document).ready(function() {
        updateRandomProducts();

        // Update products every 5 minutes
        setInterval(function() {
            updateRandomProducts();
        }, 5 * 60 * 1000);  // 5 minutes in milliseconds
    });
}

// Include jQuery in the script
const jQueryScript = document.createElement("script");
jQueryScript.src = "https://code.jquery.com/jquery-3.6.0.min.js";
document.head.appendChild(jQueryScript);
