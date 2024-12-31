let memory = 0;
let display = document.getElementById('display');

function addToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Error';
    }
}

function backspace() {
    display.value = display.value.slice(0, -1);
}

function calculateSquare() {
    display.value = Math.pow(parseFloat(display.value), 2);
}

function calculatePower() {
    display.value += '**';
}

function calculateSquareRoot() {
    display.value = Math.sqrt(parseFloat(display.value));
}

function calculateCubeRoot() {
    display.value = Math.cbrt(parseFloat(display.value));
}

function sin() {
    display.value = Math.sin(parseFloat(display.value) * Math.PI / 180);
}

function cos() {
    display.value = Math.cos(parseFloat(display.value) * Math.PI / 180);
}

function tan() {
    display.value = Math.tan(parseFloat(display.value) * Math.PI / 180);
}

function log() {
    display.value = Math.log10(parseFloat(display.value));
}

function ln() {
    display.value = Math.log(parseFloat(display.value));
}

function exp() {
    display.value = Math.E;
}

function pi() {
    display.value = Math.PI;
}

function factorial() {
    let n = parseInt(display.value);
    let result = 1;
    for(let i = 2; i <= n; i++) {
        result *= i;
    }
    display.value = result;
}

function inverse() {
    display.value = 1 / parseFloat(display.value);
}

function clearMemory() {
    memory = 0;
}

function memoryRecall() {
    display.value = memory;
}

function memoryAdd() {
    memory += parseFloat(display.value);
}