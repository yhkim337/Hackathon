const registForm = () => {
  document.getElementById("regist").style.display = "block";
  var btns = document.getElementsByName("btn");
  for ( var i in btns) { 
    btns[i].disabled = "disabled";
  }
}

const closeWin = () => {
  document.getElementById("regist").style.display = "none";
  document.body.style.background = 'rgb(255, 247, 238)';
  var btns = document.getElementsByName("btn");
  for ( var i in btns) {
    btns[i].disabled = "";
  }
}

const toggleTextbox = (checkbox) => {
  const textbox_elem = document.getElementById('my_text');
  textbox_elem.disabled = checkbox.checked ? false : true;
  if(textbox_elem.disabled) {
    textbox_elem.value = null;
  }else {
    textbox_elem.focus();
  }
}