<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guess The Number</title>

<style>
body {
    font-family: Arial, sans-serif;
    background: #121212;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    text-align: center;
    background: #1e1e1e;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(255,255,255,0.1);
}

input {
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
    border: none;
    width: 200px;
}

button {
    padding: 10px 20px;
    background: #00adb5;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #008891;
}

#message {
    margin-top: 15px;
    font-size: 18px;
}
</style>

</head>
<body>

<div class="container">
    <h1>Guess The Number 🎯</h1>
    <p>Guess a number between 1 and 100</p>

    <input type="number" id="guessInput" placeholder="Enter your guess">
    <br>
    <button onclick="checkGuess()">Guess</button>

    <p id="message"></p>
</div>

<script>
let randomNumber = Math.floor(Math.random() * 100) + 1;

function checkGuess() {
    let guess = document.getElementById("guessInput").value;
    let message = document.getElementById("message");

    if (guess < randomNumber) {
        message.textContent = "Too Low! Try Again.";
    } else if (guess > randomNumber) {
        message.textContent = "Too High! Try Again.";
    } else {
        message.textContent = "🎉 Correct! You guessed it!";
    }
}
</script>

</body>
</html>
