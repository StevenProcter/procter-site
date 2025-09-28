let current = 0;
const slides = document.querySelectorAll('.slide');
const progress = document.getElementById('progress');

function showSlide(i) {
  slides.forEach((slide, idx) => {
    slide.classList.toggle('active', idx === i);
  });
  progress.textContent = `Slide ${i + 1} of ${slides.length}`;
}

function nextSlide() {
  if (current < slides.length - 1) {
    current++;
    showSlide(current);
  }
}

function prevSlide() {
  if (current > 0) {
    current--;
    showSlide(current);
  }
}

showSlide(current); // initialize

