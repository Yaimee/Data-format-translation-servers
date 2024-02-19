import express from "express";

const app = express()

 // task create a route with the endpoint requestFastApPI
 const PORT = 8080

app.get("/expressData", (req, res) => {
    res.send({isRunning: true});
});

app.get("/fastapiData", async (req, res) => {
    const response = await fetch("https://127.0.0.1:8000/fastapiData");
    const result = await response.json();
    res.send({data: result});
});

app.post("/fastapiData", async (req, res) => {

app.listen(8080, () => console.log("Server is running on port", PORT));
