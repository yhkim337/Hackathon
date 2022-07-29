const showNoticeContent = (id) => {
  const text = document.getElementById(`notice-content-${id}`);
  if(text.style.display == "none"){
    text.style.display = "table-cell";
    text.setAttribute("colspan", "3")

  } else{
    text.style.display = "none"
  }
  
  
};