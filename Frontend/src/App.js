import React, { useState } from "react";
import DatabaseForm from "./components/DatabaseForm";
import QueryForm from "./components/QueryForm";
import QueryResults from "./components/QueryResults";
import RunQueryButton from "./components/RunQueryButton";
import "./components/styles/App.css";

function App() {
  const [dbCredentials, setDbCredentials] = useState(null);
  const [queryResults, setQueryResults] = useState(null);
  const [tableData, setTableData] = useState(null);

  return (
    <div className="App">
      <DatabaseForm setDbCredentials={setDbCredentials} />
      {dbCredentials && (
        <QueryForm
          dbCredentials={dbCredentials}
          setQueryResults={setQueryResults}
        />
      )}
      {queryResults && <QueryResults results={queryResults} />}
      {queryResults && <RunQueryButton setTableData={setTableData} />}
      {tableData && <div>{JSON.stringify(tableData)}</div>}
    </div>
  );
}

export default App;
