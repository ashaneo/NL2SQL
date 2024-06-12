import React, { useState } from "react";
import axios from "axios";
import "./styles/QueryForm.css";

function QueryForm({ dbCredentials, setQueryResults }) {
  const [question, setQuestion] = useState("");
  const [message, setMessage] = useState(null);
  const [isLoading, setIsLoading] = useState(false); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true); // Set loading to true when the request starts
    setMessage(null); // Clear previous messages when new submission starts
    try {
      const response = await axios.post("http://localhost:5000/api/question", {
        question,
      });
      setQueryResults(response.data);
      setMessage(
        <p className="message">
          Query submitted successfully and results fetched
        </p>
      );
      setIsLoading(false); // Reset loading state on success
    } catch (error) {
      console.error("Failed to submit query or fetch results", error);
      setMessage(
        <p className="message">Failed to submit query. Please try again.</p>
      );
      setIsLoading(false); // Reset loading state on failure
    }
  };

  return (
    <div className="query-form">
      <form onSubmit={handleSubmit}>
        <h2>Ask a Question</h2>
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
          placeholder="Type your SQL-related question here..."
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? "Submitting..." : "Submit Question"}
        </button>
      </form>
      {message}
    </div>
  );
}

export default QueryForm;
