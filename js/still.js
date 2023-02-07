function changeNavBg(){
    var nav = document.getElementById('nav-bar');
    var upIcon = document.getElementById('upIcon');

    var scrollContent = document.getElementById('article');
    let set = 50;
    let value = scrollContent.offsetTop + set;
    var scrollValue = window.scrollY;
    if (scrollValue >= value){
        nav.classList.remove('sticky-top');
        nav.classList.add('fixed-top');
        upIcon.classList.remove('d-none');
    }
    else{
        nav.classList.remove('fixed-top');
        nav.classList.add('sticky-top');
        upIcon.classList.add('d-none');
    }
}
window.addEventListener('scroll', changeNavBg);
