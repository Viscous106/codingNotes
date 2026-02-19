# New way react app(vite way):

## How to init react app:

npm create vite@latest

## How to use:

### how to create a html element:

```jsx
import { createRoot } from 'react-dom/client';
createRoot(document.getElementById('root')).render( 
);
```


### how to return a component:

```jsx
import { createRoot } from 'react-dom/client';
function App() {
  return (
    <div>
      <h1>Hello World</h1>
    </div>
  );
}
createRoot(document.getElementById('root')).render( 
  <App />
);
```

### 
