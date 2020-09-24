import { CREATE_USER  } from "../types";

const init = {
  email: null,
  password: null,
};

export default function test(state = init, action) {
  switch (action.type) {
    case CREATE_USER: {
      return action.payload;
    }
    default:
      return state;
  }
}
