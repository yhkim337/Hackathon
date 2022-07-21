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

// const countCheck = (obj) => {
//   var chkBox = document.getElementsByName("chk");
//   var chkCnt = 0;
//   for(var i = 0; i< chkBox.length; i++){
//     if(chkBox[i].checked){
//       chkCnt++;
//     }
//   }
//   if(chkCnt > 2){
//     alert("최대 2개까지 선택 가능합니다.");
//     obj.checked = false;
//     return false;
//   }
// }

const CountChecked = (field) => {
  var maxChecked = 2;   //선택가능한 체크박스 갯수
  var totalChecked = 0; // 설정 끝
    if (field.checked) // input check 박스가 체크되면 
        totalChecked += 1; // totalChecked 증가
    else // 체크가 아니면
        totalChecked -= 1; // totalChecked 감소

    if (totalChecked > maxChecked) { // totalchecked 수가 maxchecked수보다 크다면
        alert ("최대 2개 까지만 가능합니다."); // 팝업창 띄움
    field.checked = false;
    totalChecked -= 1;
    }
}