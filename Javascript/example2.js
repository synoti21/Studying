/**function CheckWeight(name, height, weight){
    this.userName = name;
    this.userHeight = height;
    this.userWeight = weight;
    this.minWeight;
    this.maxWeight;

    this.getInfo = function(){
        var str = "";
        str += "이름 : " + this.userName;
        str += "키 : " + this.userHeight;
        str += "몸무게 : " + this.userWeight + "<br>";
        return str;
    }

    this.getResult = function(){
        this.minWeight = (this.userHeight - 100) * 0.9 -5;
        this.maxWeight = (this.userHeight - 100) * 0.9 +5;

        if(this.userWeight > this.minWeight && this.userWeight < this.maxWeight){
            return ("정상 몸무게입니다.")
        }else if(this.userWeight > this.maxWeight){
            return ("정상 몸무게보다 초과 입니다.");
        }else{
            return ("정상 몸무게보다 미달입니다.");
        }
    }
}
var jang = new CheckWeight("장보리", 190, 89);
var park = new CheckWeight("박새론",160,49);
console.log(jang);
console.log(park);
document.write(jang.getInfo());
document.write(park.getInfo(),"<br>");
document.write(jang.getResult(),"<br>");
document.write(park.getResult(),"<br>");
document.write(jang.getResult === park.getResult);
*/