input.onButtonPressed(Button.A, function () {
    randomIndex = randint(0, 5)
    // this
    randomNumber = randint(10, 20)
    mvt = ["pushups", "jumpingjacks", "frogger", "burpees", "squats", "kneeups"]
    basic.showNumber(randomNumber)
    basic.showString("" + mvt[randomIndex], 50)
counter += 1
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Completed: ")
    basic.showNumber(counter)
})
let randomNumber = 0
let counter = 0
let mvt : string[] = []
let randomIndex = 0
counter = 0
