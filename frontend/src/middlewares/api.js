import axios from "axios";
import { GET_NOTES_LIST } from "../action_types";
import { getNotesList } from "../store/notes/actions";
import endpoints from "./api_endpoints";
import ConfigDB from "../../config";

console.log('===========')
console.log(ConfigDB.data.api.host)
console.log('===========')


const logSuccess = (res, type) => {
  if (process.env.NODE_ENV === "production") {
    return;
  }

  console.log(
    "%cAPI Response",
    "background: green; color: black",
    type,
    "\n",
    // 'URL:', res.config.url, '\n',
    "Response:",
    res,
    "\n",
    "Data:",
    res.data
  );
};

const logFailure = (err, type) => {
  if (process.env.NODE_ENV === "production") {
    return;
  }

  if (err.response !== undefined) {
    console.error(
      "%cAPI Error",
      "background: red; color: white",
      type,
      "\n",
      "Error:",
      err,
      "\n",
      // 'URL:', err.config.url, '\n',
      "Response:",
      err.response,
      "Data:",
      err.response.data
    );
  } else {
    console.error(
      "%cAPI Error",
      "background: red; color: white",
      type,
      "\n",
      "Error:",
      err,
      "\n"
      // 'URL:', err.config.url, '\n',
    );
  }
};

const handleAlternativeActions = (
  dispatch,
  type,
  payload,
  state,
  previousPayload
) => {
  if (type === GET_NOTES_LIST.concat("_SUCCESS")) {
    dispatch(getNotesList());
  }
};

const handleErrorActions = (dispatch, type) => {};

const handleApiCall = (store, action) => {
  const state = store.getState();
  const { dispatch } = store;
  const instance = axios.create();

  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      return Promise.reject(error);
    }
  );

  instance
    .request({
      baseURL:  "http://localhost:8080/",
      headers: {
        "Content-Type": "application/json",
      },
      method: endpoints[action.type].method,
      url: endpoints[action.type].endpoint(state, action),
      data:
        endpoints[action.type].payload === undefined
          ? undefined
          : endpoints[action.type].payload(state, action),
    })
    .then((res) => {
      dispatch({
        type: action.type.concat("_SUCCESS"),
        payload: res.data,
        requestAction: action,
        headers: res.headers,
      });
      logSuccess(res, action.type);
      // handleAlternativeActions(
      //   dispatch,
      //   action.type.concat('_SUCCESS'),
      //   res.data,
      //   state,
      //   action.payload,
      // );
    })
    .catch((err) => {
      dispatch({
        type: action.type.concat("_FAILURE"),
        payload: err.response,
        requestAction: action,
      });

      logFailure(err, action.type);
      handleErrorActions(dispatch, action.type);

      if (err.response !== undefined) {
        // handleErrorMessage(
        //     dispatch,
        //     err.response.data,
        // )
      }
    });
};

const logger = (store) => (next) => (action) => {
  if (action.api === true) handleApiCall(store, action);
  next(action);
};

export default logger;
