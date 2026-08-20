import { Routes, Route } from "react-router"
import HomePage from "./pages/HomePage.jsx"
import CreatePage from "./pages/CreatePage.jsx"
import NoteDetailPage from "./pages/NoteDetailPage.jsx"

const App = () => {
	return (
		<Routes>
			<Route path="/" element={<HomePage />} />
			<Route path="/create" element={<CreatePage />} />
			<Route path="/note/:id" element={<NoteDetailPage />} />
		</Routes>
	)
}
export default App
