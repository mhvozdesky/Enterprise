var sec1 =  document.querySelector('.section_1');
var sec2 =  document.querySelector('.section_2');
var sec3 =  document.querySelector('.section_3');
var sec4 =  document.querySelector('.section_4');
var sec5 =  document.querySelector('.section_5');
var sec6 =  document.querySelector('.section_6');

var section_list = [sec1, sec2, sec3,sec4, sec5, sec6];

function position_section() {
  var nearest_section = get_nearest_section();
  var indicator = document.querySelector('.data-section-to-' + nearest_section.getAttribute("class")[8]);

  
  indicators_unselected(); //let's make all indicators unselected

  indicator.style.backgroundColor = "#fff"; // виділений
  indicator.style.borderColor = "#00000080";// виділений

}

function get_nearest_section() {
  var minimum_distance = 1000000;
  var nearest_section;

  for (var i = 0; i <= 5; i++) {
    section = section_list[i];
    section_position = section.getBoundingClientRect().top;

    if (Math.max(section_position, (section_position*-1)) < minimum_distance) {
      minimum_distance = Math.max(section_position, (section_position*-1));
      nearest_section = section;
    }
  }

  return nearest_section;
}

function indicators_unselected() {
  for (var i = 0; i <= 5; i++) {
    indicator = document.querySelector('.data-section-to-' + (i+1));
    indicator.style.backgroundColor = "#ffffff80"; //indicators_unselected
    indicator.style.borderColor = "#00000033"; //indicators_unselected
  }
}

function switch_section(e) {
  var selected_element = document.querySelector('.section_' + e);
  selected_element.scrollIntoView(top); 

  position_section();

}

//Run the function when scrolling the page
window.addEventListener('scroll', function() {
  position_section();
});

position_section();