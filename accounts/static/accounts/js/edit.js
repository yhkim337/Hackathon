(() => {
    selectedControl();
  })();

function selectedControl(){
    const el = document.getElementById('army_type');
    const len = el.options.length; 
    const str = document.getElementById('searchValue').value;
    for (let i=0; i<len; i++){  
      if(el.options[i].value == str){
          el.options[i].selected = true;
      }
    }  
  }