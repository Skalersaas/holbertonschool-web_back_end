console.log("Welcome to Holberton School, what is your name?");

process.on("exit", () => {
    console.log("This important software is now closing");
});

process.stdin.on("data", data => {
    data = data.toString();
    console.log("Your name is:", data);
});
