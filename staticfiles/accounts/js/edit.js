// (() => {
//     selectedControl();
//   })();

// function selectedControl(){
//     const el = document.getElementById('army_type');
//     const len = el.options.length; 
//     const str = document.getElementById('searchValue').value;
//     for (let i=0; i<len; i++){  
//       if(el.options[i].value == str){
//           el.options[i].selected = true;
//       }
//     }  
//   }

const showfield1 = (name) => {
  if(name=='주식'){
      document.getElementById('div1').innerHTML='주식종목: <input type="text" name="stock_type" />';
  } else{
      document.getElementById('div1').innerHTML='';
  } 
};

const showfield2 = (name) => {
  if(name=='주식'){
      document.getElementById('div2').innerHTML='주식종목: <input type="text" name="stock_type" />';
  } else{
      document.getElementById('div2').innerHTML='';
  } 
};