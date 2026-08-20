import express from "express";// const express = require("express")
import notesRoutes from "./routes/notesRoutes.js";// the .js extension is required in ESM imports
import { connectDB } from "./config/db.js";// MongoDb:
import rateLimiter from "./middleware/rateLimiter.js";
import dotenv from "dotenv";//dotenv:

dotenv.config();

const app = express() // creating a basic app 
const PORT = process.env.PORT || 5001; // || 5001 is a fallback value

app.use(express.json())// middle layer if this was not here then we couldnt have used the input through forms as a variable.

app.use(rateLimiter);//rateLimiting

app.use("/api/notes", notesRoutes);

connectDB().then(() => {
	app.listen(PORT, () => {
		console.log("Server started on PORT:", PORT);
	})
})
