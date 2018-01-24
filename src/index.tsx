import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppRouter from './routers/AppRouter';
import configureStore from './store/configureStore';

const store = configureStore();

const App = () => (
  <MuiThemeProvider>
    <Provider store={store}>
      <AppRouter />
    </Provider>
  </MuiThemeProvider>
);

ReactDOM.render(<App />, document.getElementById('app'));
