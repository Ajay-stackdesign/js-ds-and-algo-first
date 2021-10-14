//To find the minimumnumber

//[4,3,1,5]
//step1 : To compare the number let array[0] be the minimum number 
//step 2 : let array[0] be the minimum number

const minimmumNumber = (array => {

    if (!array.length){
        throw new Error("array is empty");
    }else if(array.length === 0){
        return array[0];
    }else{
        let currentMin = array[0];
        for(let i=1;i<array.length;i++){
            if(array[i] < currentMin){
                currentMin = array[i];
            }
        }
        return currentMin
    }
})

const result = minimmumNumber([4,3,1,5]);
console.log(result)