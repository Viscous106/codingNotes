export function getAllNotes(req, res) {
	res.status(200).send("Successfully fetched all notes");
};

export function changeNote(req, res) {
	res.status(201).json({ message: "notes created succesfully" });
};

export function deleteNote(req, res) {
	res.status(200).json({ message: "notes were deleted succesfully" });
};

export function updateNote(req, res) {
	res.status(200).json({ message: "notes were updated successfully" });
}
