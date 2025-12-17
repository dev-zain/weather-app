// Add loading animation when form is submitted
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('weatherForm');
    const searchBtn = form.querySelector('.search-btn');
    const originalBtnText = searchBtn.innerHTML;

    form.addEventListener('submit', function() {
        // Change button text to show loading state
        searchBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
        searchBtn.disabled = true;
    });

    // Add animation to weather details on load
    const detailItems = document.querySelectorAll('. detail-item');
    detailItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
        item.style.animation = 'fadeInUp 0.5s ease-in-out forwards';
    });

    // Add enter key support
    const searchInput = document.querySelector('.search-input');
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            form.submit();
        }
    });
});