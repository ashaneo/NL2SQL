import React, { useState } from "react";
import axios from "axios";
import "./styles/DatabaseForm.css"; 

function DatabaseForm({ setDbCredentials }) {
  const [credentials, setCredentials] = useState({
    host: "",
    port: "",
    user: "",
    password: "",
    database: "",
  });
  const [passwordShown, setPasswordShown] = useState(false);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setCredentials({
      ...credentials,
      [e.target.name]: e.target.value,
    });
  };

  const togglePasswordVisibility = () => {
    setPasswordShown(!passwordShown);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await axios.post(
        "http://localhost:5000/api/db_credentials",
        credentials
      );
      setDbCredentials(credentials); // Store credentials in a parent component state
      setMessage(<p>Database credentials saved successfully!</p>);
    } catch (error) {
      console.error("Failed to save credentials", error);
      setMessage(<p>Failed to save database credentials!</p>);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="database-form">
      <h2>Enter Database Credentials</h2>
      <div className="input-group">
        <label>Host:</label>
        <input
          type="text"
          name="host"
          placeholder="Host"
          value={credentials.host}
          onChange={handleChange}
          required
        />
        <label>Port:</label>
        <input
          type="text"
          name="port"
          placeholder="Port"
          value={credentials.port}
          onChange={handleChange}
          required
        />
        <label>Username:</label>
        <input
          type="text"
          name="user"
          placeholder="Username"
          value={credentials.user}
          onChange={handleChange}
          required
        />
        <label>Password:</label>
        <div className="password-input">
          <input
            type={passwordShown ? "text" : "password"}
            name="password"
            placeholder="Password"
            value={credentials.password}
            onChange={handleChange}
            required
          />
          <span onClick={togglePasswordVisibility} className="toggle-password">
            {passwordShown ? "👁️" : "👁️‍🗨️"}
          </span>
        </div>
        <label>Database Name:</label>
        <input
          type="text"
          name="database"
          placeholder="Database Name"
          value={credentials.database}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit" className="submit-button" disabled={loading}>
        {loading ? "Saving..." : "Save Credentials"}
      </button>
      {message && <div className="message">{message}</div>}
    </form>
  );
}

export default DatabaseForm;
