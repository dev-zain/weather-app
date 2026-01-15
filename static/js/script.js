// Add loading animation when form is submitted
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('weatherForm');
    const searchBtn = form.querySelector('.search-btn');
    const originalBtnText = searchBtn.innerHTML;
    const locateBtn = document.getElementById('locateBtn');
    const latInput = document.getElementById('lat');
    const lonInput = document.getElementById('lon');
    const cityInput = document.getElementById('cityInput');

    form.addEventListener('submit', function () {
        // Change button text to show loading state
        searchBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
        searchBtn.disabled = true;
    });

    // Geolocation button handler
    locateBtn.addEventListener('click', function () {
        if (navigator.geolocation) {
            locateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Locating...';
            locateBtn.disabled = true;

            navigator.geolocation.getCurrentPosition(
                function (position) {
                    // Success - got coordinates
                    latInput.value = position.coords.latitude;
                    lonInput.value = position.coords.longitude;
                    cityInput.value = ''; // Clear city input so backend uses coords
                    form.submit();
                },
                function (error) {
                    // Error handling
                    locateBtn.innerHTML = '<i class="fas fa-location-crosshairs"></i> Use My Location';
                    locateBtn.disabled = false;

                    let errorMsg = 'Unable to get your location.';
                    if (error.code === error.PERMISSION_DENIED) {
                        errorMsg = 'Location access denied. Please enable location permissions.';
                    } else if (error.code === error.TIMEOUT) {
                        errorMsg = 'Location request timed out. Please try again.';
                    }
                    alert(errorMsg);
                },
                {
                    enableHighAccuracy: true,
                    timeout: 10000,
                    maximumAge: 300000 // Cache location for 5 minutes
                }
            );
        } else {
            alert('Geolocation is not supported by your browser.');
        }
    });

    // Add animation to weather details on load
    const detailItems = document.querySelectorAll('.detail-item');
    detailItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
        item.style.animation = 'fadeInUp 0.5s ease-in-out forwards';
    });

    // Add enter key support
    const searchInput = document.querySelector('.search-input');
    searchInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            form.submit();
        }
    });
});