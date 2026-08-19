import express from "express"

import { getAllNotes, changeNote, updateNote, deleteNote } from "../controllers/notesController.js"

const router = express.Router();

// pass the controller itself — don't wrap it in an arrow that never calls it
router.get("/", getAllNotes);


// first post request:
// 201 if creation was done success.
router.post("/", changeNote);

router.put("/:id", updateNote);

router.delete("/:id", deleteNote);


export default router

