function show_menu_modile(x){
  var a = document.querySelector('.header-menu');
  a.classList.toggle("activ");
}

function ClickListener(event){

  edit_menu_button(event);

}

function edit_menu_button(e){
  
  var header_menu = document.querySelector('.header-menu');
  var mobile_menu_button = document.querySelector('.title-menu-modile a');

  if (!header_menu.contains(e.target) && !mobile_menu_button.contains(e.target)){
    header_menu.classList.toggle("activ");
  }

}




document.addEventListener('click', ClickListener);