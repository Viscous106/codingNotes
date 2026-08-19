import mongoose from "mongoose";


// Schema:
const noteSchema = new mongoose.Schema(
	{
		title: {
			type: String,
			required: true
		},
		content: {
			type: String,
			required: true
		},
	},
	{ timestamps: true }// createdAt ,updatedAt
);

// Model:
const Note = mongoose.model("Notes", noteSchema);
export default Note
