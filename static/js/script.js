document.addEventListener("DOMContentLoaded", function() {
  setupHeader();
  setupCarousel();
  setupVideoAutoplay();
  setupSubNavbar();
});

function setupHeader() {
  const header = document.querySelector("header");
  if (header) {
      window.addEventListener("scroll", function() {
          header.classList.toggle("sticky", window.scrollY > 0);
      });
  }
}

function setupCarousel() {
  const buttons = document.querySelectorAll("[data-carousel-button]");

  buttons.forEach(button => {
      button.addEventListener("click", () => {
          const offset = button.dataset.carousel === "next" ? 1 : -1;
          const carousel = button.closest("[data-carousel]");
          const slides = carousel.querySelectorAll("[data-slide-item] .slide-item");
          const activeSlide = carousel.querySelector("[data-slide-item] .slide-item[data-active]");
          let newIndex = [...slides].indexOf(activeSlide) + offset;

          if (newIndex < 0) newIndex = slides.length - 1;
          if (newIndex >= slides.length) newIndex = 0;

          // Hide all slides
          slides.forEach(slide => {
              slide.removeAttribute("data-active");
          });

          // Set the next slide as active
          slides[newIndex].setAttribute("data-active", true);
      });
  });
}

function setupVideoAutoplay() {
  window.addEventListener("scroll", function() {
      var videoSection = document.getElementById("videoSection");
      var video = videoSection.querySelector("video");
      var rect = videoSection.getBoundingClientRect();

      // Play video when video section comes into view
      if (rect.top < window.innerHeight && rect.bottom >= 0) {
          video.play();
      } else {
          video.pause();
      }
  });
}

function setupSubNavbar() {
  let lastScrollTop = 0;
  const subNavbars = document.querySelectorAll('.sub-navbar');

  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
      // Scrolling down
      subNavbars.forEach(subNavbar => {
        subNavbar.classList.remove('locked');
      });
    } else {
      // Scrolling up
      // Optionally do something here
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For Mobile or negative scrolling
  });

  subNavbars.forEach(subNavbar => {
    subNavbar.addEventListener('mouseover', function() {
      subNavbar.classList.add('locked');
    });

    subNavbar.addEventListener('mouseout', function() {
      subNavbar.classList.remove('locked');
    });
  });
}

