function changeNavBg(){
    var nav = document.getElementById('nav-bar');
    var scrollContent = document.getElementById('article');
    let set = 50;
    let value = scrollContent.offsetTop + set;
    var scrollValue = window.scrollY;
    if (scrollValue >= value){
        nav.classList.remove('sticky-top');
        nav.classList.add('fixed-top');
    }
    else{
        nav.classList.remove('fixed-top');
        nav.classList.add('sticky-top');
    }
}
window.addEventListener('scroll', changeNavBg);
