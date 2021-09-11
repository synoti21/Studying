$(function(){
    let decCount = 0; 
    let displayResult = 0; 
    let i=0;
    
    $("ul:li(0)").click(function() { 
        displayResult = Math.pow(10,decCount)+displayResult;
        $(".cal_display").text(displayResult);
        decCount+=1;
    });
})

