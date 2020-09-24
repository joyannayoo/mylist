import React, { useState } from "react";
import { connect } from "react-redux";
import { signUpFunction } from "../../store/actions/signUp";
import styles from "./SignUp.module.scss";

const Signup = (props) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = props.dispatch;
  const history = props.history;

  const signUpHandler = (event) => {
      event.preventDefault();
      const data = {
          firstName,
          lastName,
          email,
          password
      }
    dispatch(signUpFunction(data));
    history.push("/signup");
  };


  return (
    <div className={styles.Container}>
      This is the Sign Up page
      <form className={styles.SignUpForm} onSubmit={signUpHandler}>
        First Name
        <input type="text" onChange={event => setFirstName(event.target.value)} />
        Last Name
        <input type="text" onChange={event => setLastName(event.target.value)} />
        Email
        <input type="email" onChange={event => setEmail(event.target.value)} />
        Password
        <input type="password" onChange={event => setPassword(event.target.value)} />
        <button onClick={signUpHandler}>
          Submit
        </button>
      </form>
    </div>
  );
};

export default connect()(Signup);
