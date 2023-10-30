import {
  GET_NOTES_LIST,
  POST_NOTE_CREATE,
  DELETE_NOTE,
  PUT_NOTE_UPDATE,
} from "../action_types";

const endpoints = {
  [GET_NOTES_LIST]: {
    endpoint: (state) => `/notes/`,
    method: "GET",
  },
  [POST_NOTE_CREATE]: {
    endpoint: (state) => `/notes/`,
    method: "POST",
    payload: (state, action) => action.payload,
  },
  [DELETE_NOTE]: {
    endpoint: (state, action) => `/notes/${action.payload}/`,
    method: "DELETE",
    payload: (state, action) => action.payload,
  },
  [PUT_NOTE_UPDATE]: {
    endpoint: (state, action) => `/notes/${action.payload.id}/`,
    method: "PUT",
    payload: (state, action) => action.payload.body,
  },
};

export default endpoints;
