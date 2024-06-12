import React, { useState } from "react";
import axios from "axios";
import "./styles/RunQueryButton.css"; 

function RunQueryButton() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [tableData, setTableData] = useState([]);

  const handleRunQuery = async () => {
    setIsLoading(true);
    setError("");
    try {
      const response = await axios.post(
        "http://localhost:5000/api/run_query",
        {}
      );
      setTableData(response.data);
    } catch (err) {
      setError("Failed to fetch data. Please try again.");
      console.error("Error fetching table data:", err);
    } finally {
      setIsLoading(false);
    }
  };

  const extractKeys = (data) => {
    const keys = new Set();
    data.forEach((item) => {
      Object.keys(item).forEach((key) => keys.add(key));
    });
    return Array.from(keys);
  };

  const columns = tableData.length > 0 ? extractKeys(tableData) : [];

  return (
    <div className="container">
      <button
        className="run-query-button"
        onClick={handleRunQuery}
        disabled={isLoading}
      >
        {isLoading ? "Running..." : "Run Query"}
      </button>
      {error && <p className="error-message">{error}</p>}
      <div>
        {tableData.length > 0 && (
          <table className="data-table">
            <thead>
              <tr>
                {columns.map((column, index) => (
                  <th key={index}>{column}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, index) => (
                <tr key={index}>
                  {columns.map((column) => (
                    <td key={column}>{row[column] || "N/A"}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}

export default RunQueryButton;
