import {
  NOTES_LIST,
  NOTE_CREATE,
  NOTE_DELETE,
  NOTE_UPDATE,
} from "../action_types";

const endpoints = {
  [NOTES_LIST]: {
    endpoint: (state) => `/notes/`,
    method: "GET",
  },
  [NOTE_CREATE]: {
    endpoint: (state) => `/notes/`,
    method: "POST",
    payload: (state, action) => action.payload,
  },
  [NOTE_DELETE]: {
    endpoint: (state, action) => `/notes/${action.payload}/`,
    method: "DELETE",
    payload: (state, action) => action.payload,
  },
  [NOTE_UPDATE]: {
    endpoint: (state, action) => `/notes/${action.payload.id}/`,
    method: "PUT",
    payload: (state, action) => action.payload.body,
  },
};

export default endpoints;
