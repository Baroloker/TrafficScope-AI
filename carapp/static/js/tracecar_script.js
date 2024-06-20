document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll('.slide');
    const nextButton = document.getElementById('next');
    const prevButton = document.getElementById('prev');
    let currentIndex = 0;
    const itemsPerPage = 6; // 每次显示六张

    function updateSliderPosition() {
        slides.forEach((slide, index) => {
            if (index >= currentIndex && index < currentIndex + itemsPerPage) {
                slide.classList.add('current-slide');
            } else {
                slide.classList.remove('current-slide');
            }
        });
    }

    function showNextSlides() {
        if (currentIndex + itemsPerPage < slides.length) {
            currentIndex += itemsPerPage;
        } else {
            currentIndex = 0; // 回到第一组幻灯片
        }
        updateSliderPosition();
    }

    function showPrevSlides() {
        if (currentIndex - itemsPerPage >= 0) {
            currentIndex -= itemsPerPage;
        } else {
            currentIndex = Math.max(0, slides.length - itemsPerPage); // 跳到最后一组
        }
        updateSliderPosition();
    }

    nextButton.addEventListener('click', showNextSlides);
    prevButton.addEventListener('click', showPrevSlides);

    // 初始化显示第一组幻灯片
    updateSliderPosition();
});
