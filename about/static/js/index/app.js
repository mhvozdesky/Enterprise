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
  var a = header_menu.classList;

  if (!header_menu.contains(e.target) && !mobile_menu_button.contains(e.target) && a.contains('activ')){
    header_menu.classList.toggle("activ");
  }

}

function pos_slider_description(){
	var header = document.querySelector('.header-conteiner');
	var slider_description = document.querySelector('.slider-description');
	slider_description.style.transform = "translate(0px, 0px)"; // в исходное положение

	//получить низ хедера и верх slider_description
	var header_bottom = header.getBoundingClientRect().bottom;
	var slider_description_top = slider_description.getBoundingClientRect().top;

	dif = header_bottom - slider_description_top; // на сколько slider_description вылазит за хедер

	if (dif > 0){
		slider_description.style.transform = "translate(0px, " + String(dif) + "px)";
	} else{
		slider_description.style.transform = "translate(0px, 0px)"; // в исходное положение
	}

}

function resizeListener(){
	pos_slider_description();
}




document.addEventListener('click', ClickListener);

window.onload = function() {
  pos_slider_description();
};

window.addEventListener('resize', resizeListener);

// window.addEventListener(`resize`, event => {
//   pos_slider_description();
// }, false);