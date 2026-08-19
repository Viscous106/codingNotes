import mongoose from "mongoose"

export const connectDB = async () => {
	try {
		await mongoose.connect(process.env.MONGO_URI);
		console.log("MongoDB connected");
	} catch (error) {
		console.error("Error connecting to MongoDb", error);
		process.exit(1); //1 means exit with failure
	}
}
