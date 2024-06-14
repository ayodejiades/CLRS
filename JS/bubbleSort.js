const swap = (array, i, j) => {
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

function BubbleSort(array) {
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = 0; j < array.length - i - 1; j++) {
            if (array[j] > array[j+1]) {
                swap(array, j, j+1);
            }
        }
    }
    return array; 
}

let arr = [7, 2, 8, 5];
let output = BubbleSort(arr);
console.log(output); 