import express from "express";// const express = require("express")
import notesRoutes from "./routes/notesRoutes.js";// the .js extension is required in ESM imports
import { connectDB } from "./config/db.js";// MongoDb:
import dotenv from "dotenv";//dotenv:

dotenv.config();
const app = express() // creating a basic app 
const PORT = process.env.PORT || 5001; // || 5001 is a fallback value
connectDB();

app.use("/api/notes", notesRoutes);

// first get request:
// 200 returns if it resolves safely.

/*
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
*/
app.listen(PORT, () => {
	console.log("Server started on PORT:", PORT);
})
