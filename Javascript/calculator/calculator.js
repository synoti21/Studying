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
        if(!(e.target.innerText =='0' && inputNum == '0')){ // prevents adding '0' when no input
            inputNum += e.target.innerText; // calls text in target's button. e.g) button '1' => calls '1'
            displayNum.innerText = inputNum;
            document.getElementById("clear").innerHTML = "C"; //changes 'clear all' to 'clear'
        }
       
    })
})

operationButtons.forEach(operation => {
    operation.addEventListener('click',(e) => {
         if(inputNum && savedNum && lastOperation){ //when it already done the operation at least once
             calOperate();
             if(savedNum == Infinity || displayNum.innerText == 'NaN'){
                 displayNum.innerText = "Not a Number";
             }
             lastOperation = e.target.innerText; // gets new operator for chained operation
         }else{  //initial operation
             lastOperation = e.target.innerText;
             if(inputNum) savedNum = inputNum; //starts new operation (not chained) if clicked equal button before
             inputNum = ''; // make calculator ready to get new value
         }
    })
})

function calEquation(){
    if(inputNum && savedNum && lastOperation){
        calOperate();
        result = savedNum;
        displayNum.innerText = result;
        if(result == Infinity || displayNum.innerText == 'NaN'){
            displayNum.innerText = "Not a Number";
        }
        inputNum, lastOperation = '';
    }
}

function calClear(){
    document.getElementById("clear").innerHTML = "AC"; //once cleared, change button to 'all-clear'
    if(inputNum || displayNum.innerText != '0'){ //clear display and recent inputNum data if there's input data or equated
        displayNum.innerText = '0';
        inputNum = '';
    }else{ //clear all including lastoperation, savedNum, result
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



