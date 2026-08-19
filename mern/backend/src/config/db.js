import mongoose from "mongoose"

export const connectDB = async () => {
	try {
		mongoose.connect("mongodb+srv://virulkaryashed_db_user:tR5SyPOkO0S0wZPH@cluster0.tvphpr1.mongodb.net/?appName=Cluster0");
		console.log("MongoDB connected");
	} catch (error) {
		console.error("Error connecting to MongoDb", error);
		process.exit(1); //1 means exit with failure
	}
}
