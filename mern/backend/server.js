import express from "express"

const app = express() // creating a basic app 

app.listen(5006, () => {
	console.log("Server started on PORT: 5006");
})
