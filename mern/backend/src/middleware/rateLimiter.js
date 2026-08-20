import ratelimit from "../config/upstash.js"

const rateLimiter = async (req, res, next) => {
	try {
		const { success } = await ratelimit.limit("my-limit-key");// we are supposed to use the auth details of a user instead of the my-limit-key but for now this is a dummy way to teach.
		if (!success) {
			return res.status(429).send("Too many Requests");
		}
	} catch (error) {
		console.log("Rate limit error:", error);
		next(error);
	}
	next();
};

export default rateLimiter;
