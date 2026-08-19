import express from "express"

import * as endpoints from "../controllers/notesController.js"

const router = express.Router();

// pass the controller itself — don't wrap it in an arrow that never calls it
router.get("/", endpoints.getAllNotes);

//get specific note
router.get("/:id", endpoints.getSpecificNote);

// first post request:
// 201 if creation was done success.
router.post("/", endpoints.changeNote);

router.put("/:id", endpoints.updateNote);

router.delete("/:id", endpoints.deleteNote);


export default router

