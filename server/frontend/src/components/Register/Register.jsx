import React, { useState } from "react";

function Register() {
  const [form, setForm] = useState({
    username: "",
    firstName: "",
    lastName: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("User Registered:", form);
  };

  return (
    <div style={{ width: "400px", margin: "auto", marginTop: "50px" }}>
      <h2>Register</h2>

      <form onSubmit={handleSubmit}>
        <input name="username" placeholder="Username" onChange={handleChange} /><br /><br />
        <input name="firstName" placeholder="First Name" onChange={handleChange} /><br /><br />
        <input name="lastName" placeholder="Last Name" onChange={handleChange} /><br /><br />
        <input name="email" placeholder="Email" onChange={handleChange} /><br /><br />
        <input name="password" type="password" placeholder="Password" onChange={handleChange} /><br /><br />

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;