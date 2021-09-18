const numberButtons = document.querySelectorAll('.number')
const operationButtons = document.querySelectorAll('.operation')
const equalButton = document.querySelector('.equal')
const displayNum = document.querySelector('.display1')
const clearButton = document.querySelector('.clear');


let inputNum = ''; // value that will be pushed to calculator
let savedNum = ''; // temporarily saved input value
let result = null;
let lastOperation = '';

numberButtons.forEach(number => { 
    number.addEventListener('click',(e) =>{
        if(!(e.target.innerText =='0' && inputNum == '')){
            inputNum += e.target.innerText; // calls text in target's button. e.g) button '1' => calls '1'
            displayNum.innerText = inputNum;
            document.getElementById("clear").innerHTML = "C";
        }
       
    })
})

operationButtons.forEach(operation => {
    operation.addEventListener('click',(e) => {
         if(inputNum && savedNum && lastOperation){ //when it already done the operation at least once
             calOperate();
         }else{  //first operate
             lastOperation = e.target.innerText;
             if(inputNum) savedNum = inputNum; // if equated before
             inputNum = ''; // make calculator ready to get new value
         }
    })
})

function calEquation(){
    if(inputNum && savedNum && lastOperation){
        calOperate();
        result = savedNum;
        displayNum.innerText = result;
        inputNum, lastOperation = '';
    }
}

function calClear(){
    document.getElementById("clear").innerHTML = "AC";
    if(inputNum || displayNum.innerText != '0'){ //clear recent inputNum data
        displayNum.innerText = '0';
        inputNum = '';
    }else{ //All clear including lastoperation, savedNum, result
        result = null;
        savedNum = '';
        inputNum = '';
        lastOperation = '';
    }
}

function calOperate(){
    if(lastOperation == '+'){
        savedNum = Number(savedNum) + Number(inputNum);
        displayNum.innerText = savedNum;
        inputNum ='';
    }else if(lastOperation == '-'){
        savedNum = Number(savedNum) - Number(inputNum);
        displayNum.innerText = savedNum;        
        inputNum ='';    
    }else if(lastOperation == '*'){
        savedNum = Number(savedNum) * Number(inputNum);
        displayNum.innerText = savedNum;
        inputNum ='';
    }else{
        savedNum = Number(savedNum) / Number(inputNum);
        displayNum.innerText = savedNum;
        inputNum ='';
    }
}



