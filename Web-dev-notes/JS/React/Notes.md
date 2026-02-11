# Old way react app:

## How to init react app:

npx create-react-app my-app
cd my-app
npm start

### How to add elements:
#### jsx:

```
jsx

const root = document.getElementById('root');
function app() {
  return (
    <div>
      <h1>Hello World</h1>
    </div>
  );
}
ReactDOM.render(<app />, root);
//you have to add babel to use jsx in react app

```


