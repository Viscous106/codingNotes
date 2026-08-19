import Note from "../models/Note.js"


export async function getAllNotes(req, res) {
	try {
		const notes = await Note.find();
		res.status(200).send("Successfully fetched all notes");
	} catch (error) {
		console.error("Error got while fetching all the notes", error);
		res.status(500).json({ message: "Internal Server error" });
	}
};

export async function changeNote(req, res) {
	try {
		const { title, content } = req.body;
		const note = new Note({ title: title, content: content });
		const savedNote = await note.save();

		res.status(201).json({ message: "Notes created succesfully", savedNote });
	}
	catch (error) {
		console.error("There was an error while creating the note:", error);
		res.status(500).json({ message: "Internal Server Error" });
	}
};

export async function updateNote(req, res) {
	try {
		const { title, content } = req.body;
		const updatedNote = await Note.findByIdAndUpdate(req.params.id, { title, content }, { new: true });
		if (!updatedNote) {
			return res.status(404).json({ message: "Note not found" });
		}

		res.status(200).json({ message: "notes were updated succesfully", updatedNote });
	}
	catch (error) {
		console.error("There was an error updating:", error);
		res.status(500).json({ message: "Internal Server Error" });
	}
};

export async function deleteNote(req, res) {
	try { }
	catch (error) { }
	res.status(200).json({ message: "notes were deleted successfully" });
}
