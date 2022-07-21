const showfield1 = (name) => {
    if(name=='주식'){
        document.getElementById('div1').innerHTML='주식종목: <input type="text" name="stock_type" />';
    } else{
        document.getElementById('div1').innerHTML='';
    } 
  }

const showfield2 = (name) => {
    if(name=='주식'){
        document.getElementById('div2').innerHTML='주식종목: <input type="text" name="stock_type" />';
    } else{
        document.getElementById('div2').innerHTML='';
    } 
  }