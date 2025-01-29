function toggleMenu() {
    var navMenu = document.querySelector('.nav-menu');
    var dropdownLogo = document.querySelector('.dropdown-logo img');
    var closeButton = document.querySelector('.dropdown-close-button button');
    var lineSplitter = document.querySelector('.line-splitter');

    if (navMenu.classList.contains('show')) {
        navMenu.classList.remove('show');
        navMenu.classList.add('hide');
        dropdownLogo.style.display = 'none';
        closeButton.style.display = 'none';
        lineSplitter.style.display = 'none';
    } else {
        navMenu.classList.remove('hide');
        navMenu.classList.add('show');
        dropdownLogo.style.display = 'block';
        closeButton.style.display = 'block';
        lineSplitter.style.display = 'block';
    }
}

function checkScreenSize() {
    var navMenu = document.querySelector('.nav-menu');
    var dropdownLogo = document.querySelector('.dropdown-logo img');
    var closeButton = document.querySelector('.dropdown-close-button button');
    var lineSplitter = document.querySelector('.line-splitter');

    if (window.innerWidth > 1200) {
        if (navMenu.classList.contains('show')) {
            navMenu.classList.remove('show');
            navMenu.classList.add('hide');
        }
        dropdownLogo.style.display = 'none';
        closeButton.style.display = 'none';
        lineSplitter.style.display = 'none';
    } else if (window.innerWidth <= 1200 && navMenu.classList.contains('hide')) {
        navMenu.classList.remove('hide');
    }
}

// Add event listener to check screen size on window resize
window.addEventListener('resize', checkScreenSize);

// Initial check on page load
checkScreenSize();