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

const SubscribeForm = document.getElementById('subscribe-form');

SubscribeForm.onsubmit = (e) => handleSubscribe(e);

const handleSubscribe = (e) => {
	e.preventDefault();
};

const submitSubscribeForm = () => {
	const subscribeForm = document.getElementById('subscribe-form');
    subscribeForm.submit();

};

const showCheckModal = () => {
	var myModal = new bootstrap.Modal(document.getElementById('subscribeModal'))
    const name = document.getElementById("name").value
    const birthday = document.getElementById("birthday").value
    const enterdate = document.getElementById("enter_date").value
    const news1 = document.getElementById("sub_type1").value
    const news2 = document.getElementById("sub_type2").value
    document.getElementById('subscribe-modal-body').innerHTML=`이름 : ${name} <br/> 생년월일 : ${birthday} <br/> 입영일자 : ${enterdate} <br/> 구독뉴스1 : ${news1} <br/> 구독뉴스2 : ${news2} `
    myModal.show();
};
