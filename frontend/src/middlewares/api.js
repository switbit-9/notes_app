import axios from "axios";
import ConfigDB from "../../config";
import endpoints from "./api_endpoints";

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
      baseURL: 'http://localhost:8080/',
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
