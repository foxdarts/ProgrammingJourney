//this is the app file for the memory game


const cardArray = [

    {

        name: 'fries',
        img: 'images/fries.png'


    },
    {  

        name: 'cheeseburger',
        img: 'images/cheeseburger.png'


    },
    {


        name: 'hotdog',
        img: 'images/hotdog.png'


    },
    {


        name: 'ice-cream',
        img: 'images/ice-cream.png'


    },
    {


        name: 'milkshake',
        img: 'images/milkshake.png'


    },
    {


        name: 'pizza',
        img: 'images/pizza.png'


    },
    {

        name: 'fries',
        img: 'images/fries.png'


    },
    {    

        name: 'cheeseburger',
        img: 'images/cheeseburger.png'


    },
    {


        name: 'hotdog',
        img: 'images/hotdog.png'


    },
    {


        name: 'ice-cream',
        img: 'images/ice-cream.png'


    },
    {


        name: 'milkshake',
        img: 'images/milkshake.png'


    },
    {


        name: 'pizza',
        img: 'images/pizza.png'


    }



]


cardArray.sort(() => 0.5 - Math.random()) //random sort for the array.

const gridDispaly = document.querySelector('#grid') //search the project for the thing after the #

const resultDisplay = document.querySelector('#result')

let cardsChosen = [] //array for chosen cards to check for matches

let chosenIds = [] //array for chosen card ids

let cardsMatched = []

function createBoard() {

    for (let i = 0; i < cardArray.length; i++) {

        const card = document.createElement('img') //creates images for the grid

        card.setAttribute('src', 'images/blank.png')  //assigns blank as the default card image

        card.setAttribute('data-id', i) //gives each generated card an id

        card.addEventListener('click', flipCard)
        
        gridDispaly.append(card) //loads teh images into the grid on the index page.

    }


}


function checkMatch() {

    const cards = document.querySelectorAll('#grid img') //grabs all the images from the grid tag

    const choiceOneId = chosenIds[0]  //created variables for constant refrences items

    const choiceTwoId = chosenIds[1]  //created veriable for constantly refrences items

    if (choiceOneId == choiceTwoId) {

        cards[choiceOneId].setAttribute('src', 'images/blank.png')

        cards[choiceTwoId].setAttribute('src', 'images/blank.png')

        alert('You selected the same card, try again?')

    } //this is for if you click the same area it prompts for another pick.


    else if (cardsChosen[0] == cardsChosen[1]) {

        alert('Match Found') //if the chosen cards match

        cards[choiceOneId].setAttribute('src', 'images/white.png') //makes match turn to blank spots on the board

        cards[choiceTwoId].setAttribute('src', 'images/white.png') //makes match turn to blank spots on the board

        cards[choiceOneId].removeEventListener('click', flipCard) //stops listening within space of already matched card.

        cards[choiceTwoId].removeEventListener('click', flipCard) //ditto

        cardsMatched.push(cardsChosen)

    } else {

        cards[choiceOneId].setAttribute('src', 'images/blank.png')

        cards[choiceTwoId].setAttribute('src', 'images/blank.png')

        alert('Sorry, no match')

    }   //else reset the game board

    resultDisplay.innerHTML = cardsMatched.length //shows matches on live page

    cardsChosen = []  //array for chosen cards base

    chosenIds = [] //array for cards chosen matching

    if (cardsMatched.length == cardArray.length/2) {

        resultDisplay.innerHTML = "Congrats you matched them all!"

    } //if matches is half the starting array length

}


function flipCard() {

    let cardId = this.getAttribute('data-id') //shows cwhat card is being clicked.

    cardsChosen.push(cardArray[cardId].name) //adds the chosen card to the empty array of cardsChosen

    chosenIds.push(cardId)

    this.setAttribute('src', cardArray[cardId].img) //makes it so when you chose a card the card shows its image.

    if (cardsChosen.length === 2) {

        setTimeout( checkMatch, 500)

    }

}


createBoard()
