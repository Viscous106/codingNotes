# React Batch C Notes

This document contains summarized notes from the React Batch C 2029 lectures, covering everything from the basics to advanced concepts like the Context API.

## Class 1: Introduction to React
- **What is React?** A declarative, component-based JavaScript library for building user interfaces.
- **Why React?** Reusable components, Virtual DOM, one-way data flow, and JSX syntax.
- **React.createElement**: The low-level API to describe UI before JSX. Syntax: `React.createElement(type, [props], [...children])`.
- **JSX**: JavaScript XML. Allows writing HTML-like syntax in JS. Must return a single parent, use `className` instead of `class`, and `style` takes an object.
- **ReactDOM.render**: Mounts the React tree into a real DOM node.

## Class 2: Build Tools and Setup (Vite)
- **Why Vite?** Fast dev server with Hot Module Replacement (HMR), uses ES modules, and Rollup for production builds.
- **Setup Command**: `npm create vite@latest my-app -- --template react`
- **Project Structure**:
  - `index.html`: Entry point.
  - `src/main.jsx`: Mounts the React app using `createRoot` (Replacing `ReactDOM.render` in React 18+).
- **Props**: Data passed from parent to child. Inside components, they are read-only and extracted via destructuring `({ title })`.
- **Styling**: Can be global (`index.css`) or component-scoped (e.g., `Card.css` or CSS Modules).

## Class 3: State
- **State vs Props**: State is internal data that can change and trigger re-renders. Props are read-only data passed from a parent.
- **useState Hook**: `const [value, setValue] = useState(initialValue);`
  - Always use the setter to update state (e.g., `setCount(count + 1)`). Do not mutate state directly.
- **Controlled Inputs**: Inputs whose values are driven by React state and updated via `onChange`.
- **Conditional Rendering**: Use logical AND (`&&`) or Ternary operators (`? :`) to render components conditionally.

## Class 4: List Rendering and useEffect
- **List Rendering**: Use `.map()` to iterate over arrays and return JSX.
  - **Key Prop**: Every outermost element in a map needs a unique and stable `key` (like `item.id`). Don't use the index if the list order can change.
- **useEffect Hook**: For handling side effects (fetching data, subscriptions, interacting with DOM).
  - `useEffect(() => { /* side effect */ return () => { /* cleanup */ } }, [dependencies]);`
  - Empty array `[]`: Runs once on mount.
  - State dependency `[id]`: Runs when `id` changes.
  - **Async fetching**: Define an async function *inside* the effect and call it.

## Class 5: Projects & Advanced React Concepts
- **React Router**: `<BrowserRouter>`, `<Routes>`, `<Route path="/" element={<Component />}>`.
  - Use `<Link to="/path">` instead of `<a>` tags to prevent page reloads.
- **Axios**: Used inside `useEffect` to fetch data from APIs (like TMDB).
  - `const response = await axios.get(url); setMovies(response.data.results);`
- **Tailwind CSS**: Utility-first CSS framework configured via `vite.config.js`. Used for quick styling.
- **Lifting State Up**: Moving state to a common ancestor (like `App.jsx`) to share it across multiple siblings (e.g., `Movies` and `WatchList`).
- **localStorage**: Used to persist state across refreshes (e.g., `localStorage.setItem('movies', JSON.stringify(watchlist))`).

## Class 9: Context API
- **Problem**: Prop drilling (passing props through many layers of components that don't need them, just to reach a deep child).
- **Solution**: Replaces prop drilling by providing a global state to the components that need it.
- **Steps**:
  1. **Create Context**: `export const MyContext = React.createContext();`
  2. **Provide Context**: Wrap parent with `<MyContext.Provider value={{ data, function }}>`
  3. **Consume Context**: In deep child, `const { data, function } = useContext(MyContext);`
