resize_elements();

window.addEventListener(`resize`, event => {
  //console.log("Resource conscious resize callback!");
  resize_elements();
}, false);

function resize_elements() {
	var header = document.querySelector('.header');
	header.style.fontSize = ((header.offsetWidth * 23.5) / 1903) + "px";

	var caption_lets = document.querySelectorAll('.caption-let');
	set_size_caption_let(caption_lets);

	var auto_names = document.querySelectorAll('.auto-name');
	var auto_prices = document.querySelectorAll('.auto-price');
	var auto_details = document.querySelectorAll('.auto-detail');
	var auto_items = document.querySelectorAll('.auto-item');
	set_size_auto_item(auto_names, auto_prices, auto_details, auto_items);

	//for font-size
	var cervice_contents = document.querySelectorAll('.cervice-content');
	set_size_cervice_content(cervice_contents);

	var indicators = document.querySelectorAll('.indicators');
	var text_indecators = document.querySelectorAll('.text-indecator');
	set_size_indicators(indicators, text_indecators);

	var section_4 = document.querySelector('.section_4');
	var content_block = document.querySelector('.content-block');
	var subscription = document.querySelector('.subscription');
	content_block.style.fontSize = ((section_4.offsetWidth * 2.5) / 1903) + "em";
	subscription.style.fontSize = ((section_4.offsetWidth * 16) / 1903) + "px";

	var section_5 = document.querySelector('.section_5');
	section_5.style.fontSize = ((section_5.offsetWidth * 16) / 1903) + "px";

	var section_6 = document.querySelector('.section_6');
	section_6.style.fontSize = ((section_6.offsetWidth * 16) / 1903) + "px";
}

function test() {
	alert("H " + document.documentElement.clientHeight + " W " + document.documentElement.clientWidth);
}

function set_size_auto_item(auto_names, auto_prices, auto_details, auto_items) {
	for (var i = 0; i < auto_items.length; i++) {
		auto_names[i].style.fontSize = ((auto_items[i].offsetWidth * 1.5) / 428.17) + "em";
		auto_prices[i].style.fontSize = ((auto_items[i].offsetWidth * 1.5) / 428.17) + "em";
		auto_details[i].style.fontSize = ((auto_items[i].offsetWidth * 1.5) / 428.17) + "em";
	}
}

function set_size_caption_let(caption_lets) {
	for (var i = 0; i < caption_lets.length; i++) {
		caption_lets[i].style.fontSize = ((caption_lets[i].offsetWidth * 3) / 1903) + "em";
	}
}

function set_size_cervice_content(cervice_contents) {
	for (var i = 0; i < cervice_contents.length; i++) {
		cervice_contents[i].style.fontSize = ((cervice_contents[i].offsetWidth * 2.6) / 451.98) + "em";
	}
}

function set_size_indicators(indicators, text_indecators) {
	for (var i = 0; i < indicators.length; i++) {
		text_indecators[i].style.fontSize = ((indicators[i].offsetWidth * 1) / 4) + "em";
	}
}