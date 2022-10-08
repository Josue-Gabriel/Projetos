const aparição = document.querySelectorAll('[titulos]');
const animação = 'animate';

function Scroll(){
  const windowTop = window.pageYOffset;
  aparição.forEach(function(element){
    if((windowTop) > element.offsetTop){
      element.classList.add(animação);
    }

    console.log(element.offsetTop);
  })

}

window.addEventListener('scroll', function(){
  Scroll();
})
