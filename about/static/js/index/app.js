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

function pos_nav(){
	// var nav = document.querySelector('.header-bottom');
	// nav.style.transform = "translate(0px, 0px)"; // в исходное положение
	// var nav_top = nav.getBoundingClientRect().top;

	// if (nav_top < 0){
	// 	nav.style.transform = "translate(0px, " + String((nav_top * -1)) + "px)";
	// }

	// if (nav.getBoundingClientRect().top <= 0) { // elem.getBoundingClientRect() возвращает в px координаты элемента относительно верхнего левого угла области просмотра окна браузера
	//    nav.classList.toggle("sticky");
	//  } else {
	//    nav.classList.toggle("sticky");
	//  }

	define_active_section();


}

function adapt_place_for_nav(){
	height_header_bottom_conteiner = document.querySelector('.header-bottom-conteiner').offsetHeight;
	empty_for_nav = document.querySelectorAll('.empty-for-nav');
	for (i=0; i < empty_for_nav.length; i++){
	    empty_for_nav[i].style.height = String(height_header_bottom_conteiner) + "px";
		empty_for_nav[i].style.minHeight = String(height_header_bottom_conteiner) + "px";
	}
	


	
}

function bubu(){
	

		var a = document.querySelector('.header-bottom'), b = null;  // селектор блока, который нужно закрепить
		window.addEventListener('scroll', Ascroll, false);
		document.body.addEventListener('scroll', Ascroll, false);  // если у html и body высота равна 100%
		function Ascroll() {
		  if (b == null) {  // добавить потомка-обёртку, чтобы убрать зависимость с соседями
		    var Sa = getComputedStyle(a, ''), s = '';
		    for (var i = 0; i < Sa.length; i++) {  // перечислить стили CSS, которые нужно скопировать с родителя
		      if (Sa[i].indexOf('overflow') == 0 || Sa[i].indexOf('padding') == 0 || Sa[i].indexOf('border') == 0 || Sa[i].indexOf('outline') == 0 || Sa[i].indexOf('box-shadow') == 0 || Sa[i].indexOf('background') == 0) {
		        s += Sa[i] + ': ' +Sa.getPropertyValue(Sa[i]) + '; '
		      }
		    }
		    b = document.createElement('div');  // создать потомка
		    b.style.cssText = s + ' box-sizing: border-box; width: ' + a.offsetWidth + 'px;';
		    a.insertBefore(b, a.firstChild);  // поместить потомка в цепляющийся блок первым
		    var l = a.childNodes.length;
		    for (var i = 1; i < l; i++) {  // переместить во вновь созданного потомка всех остальных потомков (итого: создан потомок-обёртка, внутри которого по прежнему работают скрипты)
		      b.appendChild(a.childNodes[1]);
		    }
		    //a.style.height = b.getBoundingClientRect().height + 'px';  // если под скользящим элементом есть другие блоки, можно своё значение
		    b.style.height = document.querySelector('.header-bottom').getBoundingClientRect().height + 'px';
		    a.style.padding = '0';
		    a.style.border = '0';  // если элементу присвоен padding или border
		  }
		  var menu = document.querySelector('.header-menu');
		  if (a.getBoundingClientRect().top <= 0) { // elem.getBoundingClientRect() возвращает в px координаты элемента относительно верхнего левого угла области просмотра окна браузера
		    b.className = 'sticky';
		    menu.classList.add('sticky-2');
		  } else {
		    b.className = '';
		    menu.classList.remove('sticky-2');
		  }
		  window.addEventListener('resize', function() {
		    a.children[0].style.width = getComputedStyle(a, '').width;
		    a.children[0].style.height = getComputedStyle(a, '').height;
		  }, false);  // если изменить размер окна браузера, измениться ширина элемента
		}
		Ascroll();

}

function adaptation_section_6(){
	var section_6 = document.querySelector('.section_6');
	var section_6_childs = section_6.children;
	var children_height = 0;

	for (var i = 0; i < section_6_childs.length; i++) {
		children_height = children_height + section_6_childs[i].offsetHeight;
	}

	if (section_6.offsetHeight < children_height){
		section_6.style.height = 'auto';
	} else{
		section_6.style.height = '';
	}
}

function navigation_indicator_size(){
	var item_text = document.querySelector('.side_navigation .item-text');
	var font_size_text = window.getComputedStyle(item_text, null).getPropertyValue('font-size');
	var circle = document.querySelectorAll('.side_navigation .circle');
	//Math.trunc(Number(font_size_text.replace('px', '')))

	for (i=0; i < circle.length; i++){
		circle[i].style.width = String(Math.trunc(Number(font_size_text.replace('px', ''))) + 'px');
		circle[i].style.height = String(Math.trunc(Number(font_size_text.replace('px', ''))) + 'px');
	}
}

function navigation_indicator_position(){
	var total_height = document.body.offsetHeight;
	var side_navigation = document.querySelector('.side_navigation');
	var height_side_navigation = document.querySelector('.side_navigation').offsetHeight;

	side_navigation.style.top = String((total_height / 2) - (height_side_navigation / 2)) + 'px';
}

function click_side_navigation(){
	var side_navigation = document.querySelector('.side_navigation');
	//это точно добавит и не задвоит класс activ, если он есть, то просто останется
	side_navigation.classList.remove('activ');
	side_navigation.classList.add('activ');
}

function deactivate_side_navigation(){
	var side_navigation = document.querySelector('.side_navigation');
	side_navigation.classList.remove('activ');
}

function define_active_section(){
	// сравним положение каждой секции. Которая ближе к 0, та и активная

	var section_name = '';
	var smallest_position = 10000000;

	var list_section = document.querySelectorAll('section');
	for (var i = 0; i < list_section.length; i++) {
		var section_position = Math.abs(list_section[i].getBoundingClientRect().top);
		if (section_position < smallest_position){
			section_name = list_section[i].id;
			smallest_position = section_position; 
		}
	}

	// на этом этапе мы знаем активную секцию, подсветим нужный индикатор
	// отключим все индикаторы
	var indicators = document.querySelectorAll('.circle');
	for (var i = 0; i < indicators.length; i++) {
		indicators[i].style.backgroundColor = '';
	}

	// включим нужный
	var indicator = document.querySelector('.indicator-' + section_name + ' .circle');
	indicator.style.backgroundColor = '#ef0023';

}



function resizeListener(){
	pos_slider_description();
	adapt_place_for_nav();
	adaptation_section_6();
	navigation_indicator_size();
	navigation_indicator_position();
	define_active_section();
}

document.addEventListener('click', ClickListener);

window.onload = function() {
  pos_slider_description();
  pos_nav();
  adapt_place_for_nav();
  bubu();
  adaptation_section_6();
  navigation_indicator_size();
  navigation_indicator_position();
  define_active_section();
};


window.addEventListener('resize', resizeListener);
window.addEventListener('scroll', pos_nav);
