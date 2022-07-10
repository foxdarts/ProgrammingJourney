// this is for rock paper scissors in javascript!


const computerChoiceDisplay = document.getElementById('Computer_Choice')  //pulls computer choice from site

const userChoiceDisplay = document.getElementById('User_Choice')  //pulls user choice from site

const resultanswerDisplay = document.getElementById('Result')  //shows resulting winner based on choices

const possibleChoices = document.querySelectorAll('button') //gathers buttons from site

let userChoice

let computerChoice

let result

possibleChoices.forEach(possibleChoices => possibleChoices.addEventListener('click', (e) => {

    userChoice = e.target.id //grabs user choice id from button as it gets clicked

    userChoiceDisplay.innerHTML = userChoice  //assigns and shows user choice in site.

    generateCompChoice() //function for generating a computer choice

    getResult()  //shows winning result

})) 



function generateCompChoice() {

    const randomNumber = Math.floor(Math.random() * possibleChoices.length) + 1  //returns a random number between 1 and the number of choices you have. adding 1 for indexing purposing

    if (randomNumber === 1) {

        computerChoice = 'Rock' //assigns 1 to rock

    }

    if (randomNumber === 2) {

        computerChoice = 'Paper' //assigns 2 to paper

    }

    if (randomNumber === 3) {

        computerChoice = 'Scissors'  //assigns 3 to scissors

    }

    computerChoiceDisplay.innerHTML = computerChoice //shows random generated choice on site

}

function getResult() { //logic for wins/loss very spelled out

    if (computerChoice === userChoice) {

        result = 'its a Draw!!'

    }

    if (computerChoice === 'Rock' && userChoice === 'Paper') {

        result = 'Player Wins'

    }

    if (computerChoice === 'Rock' && userChoice === 'Scissors') {

        result = 'Computer Wins'

    }

    if (computerChoice === 'Paper' && userChoice === 'Rock') {

        result = 'Computer Wins'

    }

    if (computerChoice === 'Paper' && userChoice === 'Scissors') {

        result = 'Player Wins'

    }

    if (computerChoice === 'Scissors' && userChoice === 'Paper') {

        result = 'Computer Wins'

    }
    if (computerChoice === 'Scissors' && userChoice === 'Rock') {

        result = 'Player Wins'

    }

    resultanswerDisplay.innerHTML = result


}