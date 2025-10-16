// portfolio_site/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Элементтерди алуу
    const hamburger = document.getElementById('hamburger-menu');
    const navLinks = document.getElementById('nav-links');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            // Класстарды кошуу/алып салуу
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
            
            // Меню ачык болгондо body'ге scroll'ду өчүрүү (UX үчүн маанилүү)
            if (navLinks.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = 'auto';
            }
        });

        // Мобилдик менюдагы шилтемелерди басканда менюну жабуу
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
                document.body.style.overflow = 'auto';
            });
        });
    }
});