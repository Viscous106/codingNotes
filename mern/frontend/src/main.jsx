import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { BrowserRouter } from 'react-router'

createRoot(document.getElementById('root')).render(
	<StrictMode>
		{/* BrowserRouter must wrap everything that uses routing.
		    It reads the URL bar and shares it with Routes/Link below. */}
		<BrowserRouter>
			<App />
		</BrowserRouter>
	</StrictMode>,
)
