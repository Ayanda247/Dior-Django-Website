document.addEventListener("DOMContentLoaded", function() {
    setupCarousel();
    setupQuotesCarousel();
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


function setupQuotesCarousel() {
    const quotesContainer = document.querySelector(".carousel-container");
    const quotes = quotesContainer.querySelectorAll(".slide-item");
    let currentIndex = 0;
    let intervalId;

    function showNextQuote() {
        quotes[currentIndex].removeAttribute("data-active");
        currentIndex = (currentIndex + 1) % quotes.length;
        quotes[currentIndex].setAttribute("data-active", true);
    }

    function startCarousel() {
        intervalId = setInterval(showNextQuote, 5000);
    }

    function stopCarousel() {
        clearInterval(intervalId);
    }

    quotesContainer.addEventListener("mouseover", stopCarousel);
    quotesContainer.addEventListener("mouseout", startCarousel);

    startCarousel(); // Start the carousel initially
}

// jQuery Code for the Quotes Carousel (You can remove this if you're not using jQuery)
$(document).ready(function () {
    let currentIndex = 0;
    const items = $('[data-slide-item] .slide-item');
    const itemCount = items.length;

    function showNextQuote() {
        items.eq(currentIndex).removeAttr('data-active');
        currentIndex = (currentIndex + 1) % itemCount;
        items.eq(currentIndex).attr('data-active', '');
    }

    setInterval(showNextQuote, 5000); // Change quote every 5 seconds
});

