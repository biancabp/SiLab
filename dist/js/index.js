function handleEdital(editalID) {
  const listaDeEditais = document.querySelectorAll('[data-edital]');
  const editalClicado = document.querySelector(`[data-edital='${editalID}']`);

  listaDeEditais.forEach((edital) => {
    if (edital != editalClicado) {
      edital.classList.add('is-close');
    }
  });

  editalClicado.classList.toggle('is-close');
}

$('.owl-carousel').owlCarousel({
  loop:true,
  margin:10,
  nav:true,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:3
      },
      1000:{
          items:5
      }
  }
})

/*===== SHOW NAVBAR  =====*/ 
const showNavbar = (toggleId, navId, bodyId, headerId) =>{
  const toggle = document.getElementById(toggleId),
  nav = document.getElementById(navId),
  bodypd = document.getElementById(bodyId),
  headerpd = document.getElementById(headerId)

  // Validate that all variables exist
  if(toggle && nav && bodypd && headerpd){
      toggle.addEventListener('click', ()=>{
          // show navbar
          nav.classList.toggle('show')
          // change icon
          toggle.classList.toggle('bx-x')
          // add padding to body
          bodypd.classList.toggle('body-pd')
          // add padding to header
          headerpd.classList.toggle('body-pd')
      })
  }
}
