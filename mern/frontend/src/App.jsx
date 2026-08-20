import { Routes, Route } from "react-router"
import HomePage from "./pages/HomePage.jsx"
import CreatePage from "./pages/CreatePage.jsx"
import NoteDetailPage from "./pages/NoteDetailPage.jsx"
import toast, { Toaster } from "react-hot-toast"
import { useToasterStore } from "react-hot-toast/headless"

const App = () => {
	return (
		<div>
			<button onClick={() => toast.success("shabbash")} className="text-red-500 p-4 bg-pink-300"> button daba mc </button>
			<Routes>
				<Route path="/" element={<HomePage />} />
				<Route path="/create" element={<CreatePage />} />
				<Route path="/note/:id" element={<NoteDetailPage />} />
			</Routes>
		</div>
	)
}
export default App
