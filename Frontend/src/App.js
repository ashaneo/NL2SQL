import React, { useState } from 'react';
import DatabaseForm from './components/DatabaseForm';
import QueryForm from './components/QueryForm';
import QueryResults from './components/QueryResults';
import './App.css';

function App() {
  const [dbCredentials, setDbCredentials] = useState(null);
  const [queryResults, setQueryResults] = useState(null);

  return (
    <div className="App">
      <DatabaseForm setDbCredentials={setDbCredentials} />
      {dbCredentials && <QueryForm dbCredentials={dbCredentials} setQueryResults={setQueryResults} />}
      {queryResults && <QueryResults results={queryResults} />}
    </div>
  );
}

export default App;
