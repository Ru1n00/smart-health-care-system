let bmiBtnBack = document.querySelector('.bmi-button-back');
let bmiBtn = document.querySelector('.bmi-button');
let bmiHeader = document.querySelector('#bmi');
let bmiCalculate = document.querySelector('.bmi-calculate');
let bmiResult = document.querySelector('.bmi-result');
let bmiCategoryEl = document.querySelector('.bmi-category');
let bmiErrorOverlay = document.querySelector('.bmi-error-overlay');
let bmiErrorText = document.querySelector('.bmi-error-text');
let bmiErrorCloseBtn = document.querySelector('.bmi-error-close-btn');

let heightEl = document.querySelector('.bmi-height');
let weightEl = document.querySelector('.bmi-weight');


bmiBtn.addEventListener('click', () => {
    let height = heightEl.value;
    let weight = weightEl.value;
    // check if height and weight are empty
    if (height === '' || weight === '') {
        customAlert('Please enter your height and weight');
        return;
    }

    // check if height and weight are numbers
    if (isNaN(height) || isNaN(weight)) {
        customAlert('Please enter numbers only');
        return;
    }
    
    // change height and weight from string to integer
    height = parseInt(height);
    weight = parseInt(weight);
    console.log(height, weight, typeof height, typeof weight)

    // check if height and weight are positive numbers
    if (height <= 0 || weight <= 0) {
        customAlert('Please enter positive numbers only');
        return;
    }

    // convert height from inches to meters
    height = height / 39.37;
    height = height.toFixed(2);

    console.log(height, weight);
    
    // calculate BMI
    let bmi = weight / (height * height);
    bmi = bmi.toFixed(2);
    console.log(bmi);
    
    bmiHeader.innerHTML = `Your BMI is ${bmi}`;
    bmiResult = document.querySelector('.bmi-result');
    let bmiCategory = "";
    if (bmi < 18.5) {
        bmiCategory = 'Underweight';
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        bmiCategory = 'Normal weight';
    } else if (bmi >= 25 && bmi <= 29.9) {
        bmiCategory = 'Overweight';
    } else if (bmi >= 30) {
        bmiCategory = 'Obesity';
    }

    bmiCalculate.classList.toggle('bmi-div-hidden');
    bmiResult.classList.toggle('bmi-div-hidden');
    bmiCategoryEl.innerHTML = bmiCategory;
});

bmiBtnBack.addEventListener('click', () => {
    bmiHeader.innerHTML = 'BMI Calculator';
    bmiCalculate.classList.toggle('bmi-div-hidden');
    bmiResult.classList.toggle('bmi-div-hidden');
});


function customAlert(alertText) {
    bmiErrorOverlay.classList.remove('bmi-div-hidden');
    bmiErrorText.innerText = alertText;
}

bmiErrorCloseBtn.addEventListener('click', () => {
    bmiErrorOverlay.classList.add('bmi-div-hidden');
})