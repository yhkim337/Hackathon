var to_top_button = document.getElementById('to-top');

to_top_button.addEventListener("click", function() {
    window.scrollTo({top:0, left:0});
    console.log('asdf');
});

const showNoticeContent = (id) => {
    const text = document.getElementById(`notice-content-${id}`);
    if(text.style.display == "none"){
        text.style.display = "table-cell";
        text.setAttribute("colspan", "3")
    } else{
        text.style.display = "none"
    }
    
};

const showReviewContent = (id) => {
    const text = document.getElementById(`review-content-${id}`);
    if(text.style.display == "none"){
        text.style.display = "table-cell";
        text.setAttribute("colspan", "3")
    } else{
        text.style.display = "none"
    }
    
};
