console.log('Hello World!')

const hamburger = document.querySelector('.shcs-hamburger-lines');
const hamburgerLine1 = document.querySelector('.shcs-line1');
const hamburgerLine2 = document.querySelector('.shcs-line2');
const hamburgerLine3 = document.querySelector('.shcs-line3');
const menuItemss = document.querySelector('.shcs-menu-items');
const logo = document.querySelector('.shcs-logo');

hamburger.addEventListener('click', () => {
    menuItemss.classList.toggle('shcs-menu-items-open');
    menuItemss.classList.toggle('shcs-menu-items-close');
    hamburgerLine1.classList.toggle('shcs-line1-active');
    hamburgerLine2.classList.toggle('shcs-line2-active');
    hamburgerLine3.classList.toggle('shcs-line3-active');
    console.log(hamburgerLine1.classList.values());
    logo.classList.toggle('shcs-logo-hide');
})