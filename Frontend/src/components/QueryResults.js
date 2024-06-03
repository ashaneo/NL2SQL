import React from "react";

function QueryResults({ results }) {
  return (
    <div>
      <h2>Query Results</h2>
      {results && (
        <div>
          <p>
            <strong>SQL Query:</strong> {results.sqlQuery}
          </p>
          <p>
            <strong>Result:</strong> {JSON.stringify(results.data)}
          </p>
        </div>
      )}
    </div>
  );
}

export default QueryResults;
