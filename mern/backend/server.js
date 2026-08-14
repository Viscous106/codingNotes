import express from "express"
// const express = require("express")

const app = express() // creating a basic app 

// first get request:
// 200 returns if it resolves safely.
app.get("/api/notes", (req, res) => {
	res.status(200).send("you got your first response");
})

// first post request:
// 201 if creation was done success.
app.post("/api/notes", (req, res) => {
	res.status(201).json({ message: "notes created succesfully" });
})

app.put("/api/notes/:id", (req, res) => {
	res.status(200).json({ message: "notes updated successfully" });
})

app.delete("/api/notes/:id", (req, res) => {
	res.status(200).json({ message: "notes deleted succefully" });
})

app.listen(5006, () => {
	console.log("Server started on PORT: 5006");
})
