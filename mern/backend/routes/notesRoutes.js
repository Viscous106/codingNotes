import express from "express"

const router = express.Router();

router.get("/", (req, res) => {
	res.status(200).send("you got your first response");
})

// first post request:
// 201 if creation was done success.
router.post("/", (req, res) => {
	res.status(201).json({ message: "notes created succesfully" });
})

router.put("/:id", (req, res) => {
	res.status(200).json({ message: "notes updated successfully" });
})

router.delete("/:id", (req, res) => {
	res.status(200).json({ message: "notes deleted succefully" });
})


export default router

