const swap = (array, i, j) => {
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

function SelectionSort(array) {
    for (let i = 0; i < array.length - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < array.length; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j; 
            }
        }
        if (minIndex !== i) {
            swap(array, i, minIndex);
        }
    }
    return array; 
}

let arr = [7, 2, 8, 5];
let output = SelectionSort(arr);
console.log(output); 