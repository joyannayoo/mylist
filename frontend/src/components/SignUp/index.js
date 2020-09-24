import React, { useState } from "react";
import { connect } from "react-redux";
import { signUpFunction } from "../../store/actions/signUp";
import styles from "./SignUp.module.scss";

const Signup = (props) => {
  const [email, setEmail] = useState("");

  const dispatch = props.dispatch;
  const history = props.history;

  const signUpHandler = () => {
    dispatch(signUpFunction());
    history.push("/signup");
  };

  return (
    <div className={styles.Container}>
      This is the Sign Up page
      <form className={styles.SignUpForm}>
        First Name
        <input type="text" />
        Last Name
        <input type="text" />
        Email
        <input type="email" />
        Password
        <input type="password" />
        <button type="submit" onClick={signUpHandler}>
          Submit
        </button>
      </form>
    </div>
  );
};

export default connect()(Signup);
