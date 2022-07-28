const showfield1 = (name) => {
    if(name=='주식'){
        document.getElementById('div1').innerHTML='주식종목: <input type="text" name="stock_type" placeholder="정확한 주식 종목을 입력하세요" style="font-size: 15px"/>';
    } else{
        document.getElementById('div1').innerHTML='';
    }
    const el = document.getElementById('sub_type2');
    const len = el.options.length; 
    for (let i=0; i<len; i++){  
        if(el.options[i].value == name){
            el.options[i].hidden = true;
        } else{
            el.options[i].hidden = false;
        }
    }  
};

const showfield2 = (name) => {
    if(name=='주식'){
        document.getElementById('div2').innerHTML='주식종목: <input type="text" name="stock_type" placeholder="정확한 주식 종목을 입력하세요" style="font-size: 15px"/>';
    } else{
        document.getElementById('div2').innerHTML='';
    } 
};