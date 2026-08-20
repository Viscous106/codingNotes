import { Ratelimit } from "@upstash/ratelimit"
import { Redis } from "@upstash/redis"
import { dotenv } from "dotenv"

dotenv.config();
//creating a rate limiter as 10 req is 20 sec.
const ratelimit = new Ratelimit({
	redis: Redis.fromEnv(),
	limiter: Ratelimitu.slidingWindow(10, "20 s")
});

export default ratelimit;
